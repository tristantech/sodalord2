from models import AdminUser, CustomerUser, MachineUser, User, UserAttribute, Transaction, Base

import sqlalchemy
import sqlalchemy.orm

import code

db_engine = sqlalchemy.create_engine("sqlite:///database.db")
print Base
Base.metadata.create_all(db_engine)
db = sqlalchemy.orm.sessionmaker(bind=db_engine)()

banner_str  = "Database Model Command Line\n"
banner_str += "=======================\n"
banner_str += "Warning, this provides unrestricted access to the database models!\n"



# Run an interactive Python shell.
code.interact(local=locals(), banner=banner_str)

print "Closing database session..."
db.close()