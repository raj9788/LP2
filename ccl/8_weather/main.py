import webapp2
import urllib2
import json

# https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m
class MainPage(webapp2.RequestHandler):

	def write(self,message):
		message = "<div> " + str(message) + "</div>"
		self.response.write(message)
		
	def get(self):
		htmlbody = """
		<html>
			<body>
				<h1>Enter Latitude(-90 to 90) and Longitude(-90 to 90)</h1>
				
				<form action="/result" method="post">
					Latitude :: <input type="number" name="latitude" required>
					Longitude:: <input type="number" name="longitude" required>
					<input type="submit" value"submit">
				</form>
			</body>
		</html>
		"""
		self.write(htmlbody)
		
		
class ResultPage(webapp2.RequestHandler):

	def write(self,message):
		message = str(message)
		self.response.write(message)
		
	def post(self):
		latitude = self.request.get('latitude')
		longitude = self.request.get('longitude')
		self.write(longitude)
		self.write(latitude)
		print("latitude :: ", latitude)
		print("Longitude:: ",longitude)
		url = "https://api.open-meteo.com/v1/forecast?latitude="+str(latitude)+  "&longitude="+str(longitude)+"&hourly=temperature_2m"
		response = urllib2.urlopen(url).read()
		data=json.loads(response)
		print(data)
		self.write("""
		<table style="padding:10px;margin:10px;">
		<tr>
			<td>Time</td>
			<td>Temperature</td>
		</tr>
		""")
		for d in range(len(data['hourly']['temperature_2m'])):
			temp 	= data['hourly']['temperature_2m'][d]
			time = data['hourly']['time'][d]
			self.write("<tr><td>"+str(temp)+"</td>"+" <td>  "+str(time)+"</td></tr>")
		self.write("</table>")
		
app = webapp2.WSGIApplication([("/",MainPage),('/result',ResultPage)],debug=True)
