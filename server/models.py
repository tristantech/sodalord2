import bcrypt
import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import settings

Base = declarative_base()

class User(Base):
	""" A user object for each registered sodalord customer. """

	__tablename__ = "users"
	
	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String)
	username = Column(String)
	password = Column(String) # Salted & hashed using bcrypt
	active = Column(Integer)
	deleted = Column(Integer)
	account_type = Column(String)
	timestamp = Column(DateTime)
	transactions_in = relationship("Transaction", back_populates="user_to")
	transactions_out = relationship("Transaction", back_populates="user_from")
	attributes = relationship("UserAttribute", back_populates="user")

	# Various account types exist:
	#  ADMIN:		Administrator accounts that have the power create arbitary transactions.
	#  CUSTOMER:	Ordinary users of the machine. Limited privileges.
	#  MACHINE:		Non-human users, such as the Sodalord account.
	ADMIN = "admin"
	CUSTOMER = "customer"
	MACHINE = "machine"
	__mapper_args__ = {"polymorphic_on": account_type}


	def get_balance(self):
		""" Computes the user's balance in cents by subtracting out-transactions from in-transactions. """
		return sum(map(lambda t: t.amount, self.transactions_in)) - sum(map(lambda t: t.amount, self.transactions_out))

	def check_password(self, passwd):
		""" Checks a user-provided password. Returns True if correct. """
		return bcrypt.checkpw(passwd.encode("utf8"), self.password.encode("utf8"))

	def set_password(self, old_pass, new_pass):
		""" Sets a new password. Old password must be provded unless current password is None. """
		if self.password is None or self.check_password(old_pass):
			self.password = bcrypt.hashpw(new_pass.encode("utf8"), bcrypt.gensalt().encode("utf8"))
			return True
		return False

	def get_attr(self, k):
		""" Returns a list of values with key `k`. Returns None list if key not found. """
		attr = filter(lambda a: a.key==k, self.attributes)
		return None if len(attr) == 0 else attr

	def __str__(self):
		return "[User: %s, %s, %s]".format(self.name, self.username, self.email, self.account_type)

	def get_dict(self):
		""" Returns a dict with select info on this user. """
		output = {}
		for att in ("name","username","email","account_type","id"):
			output[att] = getattr(self, att)
		return output

	@staticmethod
	def validate_username(username):
		return username and re.match(settings.REGEX_USERNAME, username)
	
	@staticmethod
	def validate_name(name):
		return name and re.match(settings.REGEX_NAME, name)

	@staticmethod
	def validate_email(email):
		return email and re.match(settings.REGEX_EMAIL, email)

class AdminUser(User):
	__mapper_args__ = {'polymorphic_identity': User.ADMIN}

class CustomerUser(User):
	verified = Column(Integer) # Gets set after email confirmation step.
	__mapper_args__ = {'polymorphic_identity': User.CUSTOMER}

class MachineUser(User):
	__mapper_args__ = {'polymorphic_identity': User.MACHINE}

class UserAttribute(Base):
	""" Stores additional user properties, such as aliases and barcodes/cards. """
	
	__tablename__ = "users_attributes"
	
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	user = relationship("User", back_populates="attributes")
	key = Column(String)
	value = Column(Text)

	def __str__(self):
		return "%s: %s".format(self.key, self.value)

class Transaction(Base):
	""" Records all transactions between users. """
	
	__tablename__ = "ledger"
	
	id = Column(Integer, primary_key=True)
	timestamp = Column(DateTime)
	
	user_from_id = Column(Integer, ForeignKey('users.id'))
	user_from = relationship("User", back_populates="transactions_out")

	user_to_id = Column(Integer, ForeignKey('users.id'))
	user_to = relationship("User", back_populates="transactions_in")

	amount = Column(Integer) # In cents. Must be positive.
	
	notes = Column(Text)
	details = Column(Text)

	def dollars(self):
		return self.amount/100.0

	def __str__(self):
		return "[Transaction: %d from (%s) to (%s)]".format(self.dollars(), user_from.name, user_to.name)
		
	