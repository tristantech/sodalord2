
import datetime

class User(Base):
	""" A user object for each registered sodalord customer. """

	__tablename__ = "users"
	
	id = Column(Integer, primary_key=True)
	name = Column(String, max_length=100)
	email = Column(String, max_length=100)
	username = Column(String, max_length=20)
	password = Column(String, max_length=100) # Salted & hashed using bcrypt
	active = Column(Boolean)
	deleted = Column(Boolean)
	admin = Column(Boolean)
	
	REGEX_USERNAME = r"[a-z0-9_]{1,20}"
	REGEX_NAME = r"[A-Za-z\ \-]{1,100}"
	
	def get_balance(self):
		""" Computes the user's balance in cents. """
		bal = 0
		return bal
	
	
	@static_method
	def get_user(username):
		""" Get a user by username, or None if they don't exist. """
		return self.db.Query(User).filter(User.username==username).one_or_none()
	
	@static_method
	def validate_username(username):
		pass
	
	@static_method
	def validate_name(name):
		pass

class UserAttribute(Base):
	""" Stores additional user properties, such as aliases and barcodes/cards. """
	
	__tablename__ = "users_attributes"
	
	id = Column(Integer, primary_key=True)
	user = Column() #TODO: Foreign key
	key = Column(String, max_length=200)
	value = Column(Text)

class Transaction(Base):
	""" Records all transactions between users. """
	
	__tablename__ = "ledger"
	
	id = Column(Integer, primary_key=True)
	timestamp = Column(DateTime)
	
	account_from = Column(ForeignKey) #TODO: foreign keys
	account_to = Column(ForeignKey)
	amount = Column(Integer) # In USD Cents. Must be positive.
	
	notes = Column(Text)
	details = Column(Text)
	
	@static_method
	def transaction(username_from, username_to, amount, **kwargs):
		""" Attempts to perform a transaction between the two users. """
		
		if type(amount) != int or amount <= 0:
			raise ValueError("Amount must be an integer and greater than zero.")
		
		# TODO: Set up a database transaction to make this atomic. Make sure it
		# 		 properly aborted after an exception.
		# TODO: Validate usernames against our regex?
		# TODO: Use more descriptive exceptions.
		
		# Check that username_from exists and has sufficient funds.
		user_from = User.get_user(username_from)
		if not user_from:
			raise Exception("User `%s` cannot be found.".format(username_from))
		if not user_from.get_balance() >= amount:
			raise Exception("User `%s` has insufficient funds. (Current balance = $%d)".format(
				user_from.username,
				user_from.get_balance()/100.0
			))
		
		# Check that the receiving user exists
		user_to = User.get_user(username_to)
		if not user_to:
			raise Exception("User `%s` cannot be found.".format(username_from))
		
		# Make the transaction.
		t = Transaction()
		t.account_from = user_from
		t.account_to = user_to
		t.amount = amount
		t.timestamp = datetime.datetime.now()
		t.notes = kwargs.get("notes")
		t.details = kwargs.get("details")

		#TODO: commit here


		
	