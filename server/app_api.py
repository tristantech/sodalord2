from models import User, Transaction

def response(success, data):
	""" Builds a JSON response object to return to the client. If `success` is True, `data` is the payload. If
	`success` is False, `data` is an error message string. """
	if success:
		return {"success": True, "message": None, "data": data}
	else:
		return {"success": False, "message": data, "data": None}

def logged_in():
	return cherrypy.session.get("logged_in", False)

def is_admin():
	return logged_in() and "user" in cherrypy.session and cherrypy.session["user"]["account_type"] == User.ADMIN

class API(object):
	""" CherryPy application that serves a JSON-based API for performing transactions. """

	@property
	def db(self):
		""" Shortcut for accessing our database session. """
		return cherrypy.request.db
	
	@cherrypy.tools.json_out()
	def test(self):
		""" Dummy endpoint for testing connectivity to the server. """
		return response(True, None)
	
	@cherrypy.tools.json_out()
	def login(self, username, password):
		""" 
		Logs in a customer. Returns a session key that should be 
		included in future requests.
		"""
		# Check username
		if not User.validate_username(username):
			return response(False, "Incorrect username or password.")

		# Find an account with this username
		user = self.db.query(User).filter(User.username==username).filter(User.deleted==0).one_or_none()
		if user is None or not user.check_password(password):
			# Unauthorized!
			return response(False, "Incorrect username or password.")

		if user.active == 0:
			return response(False, "This user account is not active.")

		# Success!
		user_dict = user.get_dict()
		cherrypy.session["logged_in"] = True
		cherrypy.session["user"] = user_dict

		return response(True, {"user": user_dict, "session": cherrypy.session["sid"]})

	@cherrypy.tools.json_out()
	def logout(self, session):
		""" Destroy this session. """
		cherrypy.session["logged_in"] = False
		cherrypy.session["user"] = None
		return response(True, {})

	@cherrypy.tools.json_out()	
	def check_balance(self, username):
		""" Checks a user's balance. Must be admin to query somebody else's balance. """
		if not logged_in():
			return response(False, "Must be logged in")

		if username != cherrypy.session["user"]["username"] and not is_admin():
			return response(False, "Only an adminsitartor may check balance of others.")

		# Get user
		user = self.db.query(User).filter(User.username==username).filter(User.deleted==0).one_or_none()
		if user is None:
			return response(False, "User not found.")

		return response(True, {"balance": user.get_balance(), "active": user.active})

	@cherrypy.tools.json_in()
	@cherrypy.tools.json_out()
	def create_account(self):
		""" Creates a new custom user account. """
		data = cherrypy.request.json

		if not all(map(lambda x: x in data, ("name", "username", "email", "password"))):
			return response(False, "Incorrectly formatted input data.")

		# Validate inputs
		if not User.validate_username(data["username"]):
			return response(False, "Invalid chosen username.")
		if not User.validate_name(data["name"]):
			return response(False, "Invalid chosen name.")
		if not User.validate_email(data["email"]):
			return response(False, "Invalid email.")

		# Create the account
		user = CustomerUser()
		user.name = data["name"]
		user.username = data["username"]
		user.email = data["email"]
		user.deleted = 0
		user.verified = 0 	# Gets set after email confirmation.
		user.active = 0 	# Gets set after email confirmation.
		user.set_password(None, data["password"])

		self.db.add(user)
		self.db.commit()

		return response(True, {"user_id": user.id})


	@cherrypy.tools.json_in()
	@cherrypy.tools.json_out()
	def make_transaction(self):
		"""
		Receives a JSON object via POST of the form:
		{
			"username_from" : <username>,
			"username_to" : <username>,
			"amount" : <integer (cents)>,
			"notes" : <string>,
			"details" : <string>
		}
		"""
		pass