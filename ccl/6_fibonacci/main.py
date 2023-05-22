import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		count = 8 
		a=0
		b=1
		for i in range(count):
			
			message = "<div> "+ str(i+1) +" number = " + str(a) + "</div> <br>"
			self.response.write(message)
			c=a+b
			a=b
			b=c
			
app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
