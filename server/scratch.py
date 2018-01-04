	@staticmethod
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