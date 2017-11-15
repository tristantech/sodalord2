from models import User, Transaction

class API(object):
	""" CherryPy application that serves a JSON-based API for performing transactions. """
	
	def test(self):
		""" Dummy endpoint for testing connectivity to the server. """
		return "OK"
	
	def login(self, username, password):
		""" 
		Logs in a customer. Returns a session key that should be 
		included in future requests.
		"""
		pass
	
	def logout(self, session):
		""" Destroy this session. """
		pass
	
	def check_balance(self, session, username):
		""" Checks a user's balance. Must be admin to query somebody else's balance. """
		pass
	
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