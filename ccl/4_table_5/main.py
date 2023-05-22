import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		table = 5
		for i in range(1,11):
			message = "<div> 5 x " + str(i) + " = " + str(i*table) + "</div>"
			self.response.write(message)
			
app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
