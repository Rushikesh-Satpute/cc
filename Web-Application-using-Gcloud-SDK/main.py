import os
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)