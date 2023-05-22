import webapp2
	
class MainPage(webapp2.RequestHandler):

	def get(self):
		count = 5
		for i in range(count):
			name = "<div> Your Name<div>"
			rollNo = "<div> Your Roll No</div>"
			depart = "<div> Your Department</div>"
			self.response.write(name+rollNo+depart + "</br>")
			

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
