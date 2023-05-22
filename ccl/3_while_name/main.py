import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		i=0
		count = 5
		while i<count:
			message = "<div>Your Name</div> <div>Your RollNo</div> <div>Your Department</div><br>"
			self.response.write(message)
			i+=1

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
