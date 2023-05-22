import webapp2 # this is the only module require

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write("<h1 style='font-size:100px;'>HELLO WORLD</h1>")
		

# WSGI = Web Server Gateway Interface 
app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
	
	
	
