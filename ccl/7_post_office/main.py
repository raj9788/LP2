import webapp2
import urllib2
import json


class MainPage(webapp2.RequestHandler):
    def get(self):

        self.response.write('<html><body>')
        self.response.write('<h1>Find Nearest Post Office</h1>')
        self.response.write('<form action="/result_1" method="post">')
        self.response.write(
            'Zip Code: <input type="text" name="zipcode"><br><br>')
        # self.response.write('Branch Name: <input type="text" name="branch" required><br><br>')
        self.response.write('<input type="submit" value="Submit">')
        self.response.write('</form></body></html>')


class ResultPage_1(webapp2.RequestHandler):
    def post(self):
        zipcode = self.request.get('zipcode')
        branch = self.request.get('branch')
        if len(zipcode) != 6 or not zipcode.isdigit():
            self.response.write('<html><body><h1>Error</h1>')
            self.response.write(
                '<p>Please enter a valid 6-digit zip code.</p>')
            self.response.write(
                '<a href="/">Go back to form</a></body></html>')
        else:
            url = 'https://api.postalpincode.in/pincode/' + zipcode
            response = urllib2.urlopen(url).read()
            # converts json to python dictationary
            data = json.loads(response)

            # self.response.write(str(data));
            if data[0]['Status'] == 'Error':
                self.response.write('<html><body><h1>Error</h1>')
                self.response.write('<p>' + data[0]['Message'] + '</p>')
                self.response.write(
                    '<a href="/">Go back to form</a></body></html>')
            else:
                # found = False
                post = data[0]['PostOffice']
                # post_office=post[0]
                # if branch.lower() in post_office['Name'].lower():
                self.response.write('<html><body><h1>Nearest Post Office</h1>')
                for i in range(len(post)):

                    self.response.write(str(i+1) + " )")
                    self.response.write('<p>Pincode: ' + zipcode + '</p>')
                    self.response.write('<p>Name: ' + post[i]['Name'] + '</p>')
                    # self.response.write('<p>Pin Code: ' + post_office['PINCode'] + '</p>')
                    self.response.write(
                        '<p>Branch Type: ' + post[i]['BranchType'] + '</p>')

                    self.response.write(
                        '<p>District: ' + post[i]['District'] + '</p>')
                    self.response.write(
                        '<p>Division: ' + post[i]['Division'] + '</p>')
                    self.response.write(
                        '<p>State: ' + post[i]['State'] + '</p>')
                    self.response.write('</body></html>')
                # found = True


app = webapp2.WSGIApplication(
    [('/', MainPage), ('/result_1', ResultPage_1)], debug=True)


# py google-cloud-sdk/bin/dev_appserver.py C:\Users\sahil\CCL_trial\7\app.yaml


'''
YOU CAN REMOVE THE CODE BELOW 
'''

# import webapp2
# import urllib2
# import json


# class MainPage(webapp2.RequestHandler):
# 	def get(self):
# 		htmlForm = """
# 		<html>
# 		<body>
# 			<form action='/result' method="post">
# 				Enter PinCode :: <input type="text" name="zipcode" required>
# 				<input value="submit" type="submit">
# 			</form>
# 		</body>
# 		</html>
# 		"""
# 		self.response.write(htmlForm)

# class ResultPage(webapp2.RequestHandler):
# 	def post(self):
# 		zipcode = self.request.get('zipcode')
# 		isCorrect = True
# 		for i in zipcode:
# 			if i<='0' or i>='9':
# 				isCorrect=False
# 				break
# 		self.response.write("<h1>"+str(not isCorrect)+"</h1><br>")
# 		if len(zipcode)!=6 and not isCorrect:
# 			self.response.write("""
# 			<html>
# 			<body>
# 				<h1>Error Occurred</h1>
# 				<a href='/'>Try Again</a>
# 			</body>
# 			</html>
# 			""")
# 		else:
# 			url = "https://api.postalpincode.in/pincode/"+zipcode
# 			response = urllib2.urlopen(url)
# 			data=response.read()
# 			jsondata = json.loads(data)
# 			for data in jsondata[0]['PostOffice']:
# 				name=data['Name']
# 				pincode=zipcode
# 				BranchType =data["BranchType"]
# 				DeliveryStatus=data["DeliveryStatus"]
# 				self.response.write("Name           ::  " + name+'<br>')
# 				self.response.write("Pincode    ::  "+pincode+'<br>')
# 				self.response.write("BranchType ::  "+BranchType+'<br>')
# 				self.response.write("Delivery   :: "+DeliveryStatus+'<br>')

# 			#self.response.write(jsondata)


# app = webapp2.WSGIApplication([('/',MainPage),('/result',ResultPage)],debug=True)
