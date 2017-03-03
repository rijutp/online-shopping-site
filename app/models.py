from app import db
class Register(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(128))
	email = db.Column(db.String(128))
	password = db.Column(db.String(128))
	is_supervisor = db.Column(db.Boolean)
 
	def __init__(self, username, email, password):
		# self.email = email
		# self.user_id = user_id
		self.username = username
		self.email = email
		self.password = password
	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.user_id)

	def user_loader(user_id):
		return User.query.get(user_id)

	def __rep__(self):
		return '<User %r>' % (self.username)

class Items(db.Model):
	item_id = db.Column(db.Integer, primary_key=True)
	itemname = db.Column(db.String(128))
	price = db.Column(db.Integer)
	description = db.Column(db.String(128))

	def __init__(self, itemname, price, description):
		self.itemname = itemname
		self.price = price
		self.description = description
	
	# def is_authenticated(self):
	# 	return True

	



# Base.metadata.create_all(bind=engine)
