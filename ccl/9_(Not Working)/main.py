import webapp2
import urllib2
import json
import requests_toolbelt.adapters.appengine
import requests


class MainPage(webapp2.RequestHandler):

    def write(self, text):
        self.response.write("<div>" + str(text) + "</div>")

    def get(self):
        html = """
		<html>
			<body>
				<h1>Enter Anime name</h1>
				<form action="/result" method="post">
					Film Name :: <input type="text" method="post" name="anime_name" required>
					<input type="submit" value"submit">
				</form>
			</body>
		</html>
		"""
        self.write("HELLO WORLD")
        self.write(html)


class ResultPage(webapp2.RequestHandler):

    def write(self, text):
        self.response.write("<div>" + str(text) + "</div>")

    def post(self):
        anime_name = self.request.get('anime_name')
        print(anime_name)
        self.write(anime_name)
        url = "https://myanimelist.p.rapidapi.com/anime/search/"+anime_name
        headers = {
            "X-RapidAPI-Key": "466ebc41e5mshf91d55ee8227c4ep1a508bjsned7ee91f2c5b",
            "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        print(response.json())
        # data = response.read()
        data = response.json()
        self.write(data)


app = webapp2.WSGIApplication(
    [("/", MainPage), ('/result', ResultPage)], debug=True)
