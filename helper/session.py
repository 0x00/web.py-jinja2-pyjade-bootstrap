import web
import hashlib
import random

class Sessions:

	def __init__(self):
		self.sessions = {}

	def session(self):
		sid = web.cookies().get("ssid")
		return self.sessions.get(sid)

 	def get(self,name):
		s = self.session()
		if s is not None:
			return s.get(name)
		return None

	def put(self,name,value):

		session = self.session()
		if session is None:
			key = hashlib.sha1(str(random.random())).hexdigest()
			web.setcookie("ssid",key,3600*24)		
			self.sessions[key] = {}
			session = self.sessions[key]
		
		session[str(name)]=str(value)
		
