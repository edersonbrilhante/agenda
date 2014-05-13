from datetime import datetime


class Event(object):
	"""docstring for Event"""
	def __init__(self, arg):
		super(Event, self).__init__()
		self.arg = arg
		self.name = arg["name"]
		self.adress = arg["adress"]
		if type(pessoa['date']).__name__ == 'datetime':
			self.date = arg["date"]
		else
		   self.date = datetime.strptime(pessoa['date'], '%Y-%m-%d')

		self.image = arg["image"]
		self.short_description = arg["short_description"]
		self.description = arg["description"]
		self.user = arg["user"]
		self.include_date = datetime.now()
		self.last_change = None
		self.last_user_change = None

		self.save()


	def save(self):
		pass

