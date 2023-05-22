import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		table = 10
		count = 10
		for i in range(0,count):
			message = "<div> "+str(table)+" x " + str(i+1)+" = "+ str((i+1)*table) + "</div>"
			self.response.write(message)
			
app = webapp2.WSGIApplication([("/",MainPage)],debug=True)	
			 
