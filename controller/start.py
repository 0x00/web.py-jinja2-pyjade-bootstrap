import template

class index:
	def GET(self):
		return template.load("index.jade").render(activetab='start')


class one:
	def GET(self):
		return template.load("index.jade").render(activetab='bla1')

class two:
	def GET(self):
		return template.load("index.jade").render(activetab='bla2')
