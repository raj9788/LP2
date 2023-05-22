
import webapp2
import json
import urllib2
# 'http://universities.hipolabs.com/search?name=[name of the university]'


class MainPage(webapp2.RequestHandler):
    def write(self, text):
        self.response.write("<div> " + str(text) + "</div>")

    def get(self):
        html = """
		<html>
			<head>
				<title>Post Office Finder</title>
				<style>
					h1{
						color:red
					}
					.form{
						font-size:25px;
						padding:10%;
					}
				</style>
			</head>
			<body>
				<div class="form">
					<form action="/result" method="post">
					Enter University Name:: <input type="text" name="university_name" required>
					<br><br>
					<input type="submit" value="Submit">
					
					</form>
				</div>
			</body>
		</html>
		"""
        self.write(html)


class ResultPage(webapp2.RequestHandler):

    def write(self, text):
        self.response.write((text))

    def post(self):
        university_name = self.request.get("university_name")
        print("\n\n\n\n\n " + university_name + "\n\n\n\n\n")
        self.write(university_name)
        url = "http://universities.hipolabs.com/search?name={}".format(
            university_name)
        response = urllib2.urlopen(url)
        html = response.read()
        data = json.loads(html)
        length = len(data)
        print(data)
        print(response.code)
        print(length)
        if response.code != 200 or length < 2:
            errorhtml = """
			<html>
			<head>
				<title>Post Office Finder</title>
				<style>
					h1{
						color:red
					}
				</style>
			</head>
			<body>
				<h1>Error Occured</h1>
				<br>
				<a href='/'>Try Again</a>
			</body>
		</html>
			"""
            self.write(errorhtml)
        else:
            for i in data:
                country = i['country']
                code = i['domains'][0]
                uni_url = i['web_pages'][0]
                name = i['name']

                self.write("<p>Country :: " + country + "</p>")
                self.write("<p>code:: " + code + "</p>")
                self.write("<p>uni_url:: " + uni_url + "</p>")
                self.write("<p>name:: " + name + "</p>")
                self.write(
                    "----------------------------------------------------------------------------------------------------<br><br>")


app = webapp2.WSGIApplication(
    [("/", MainPage), ('/result', ResultPage)], debug=True)
