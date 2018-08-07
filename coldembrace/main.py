import webapp2
from random import shuffle
import jinja2
import os


#libraries for APIs
from google.appengine.api import urlfetch
import json


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
class HomePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write("This is the home page")
   


class LoginPage(webapp2.RequestHandler):
    def get(self):
        #about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write("This is the login page")
        
        
    '''
    def post(self):
        isError = False
        if (isError):
            self.response.write("Error!")
        else:
            self.redirect("/")
    '''
    
class SurveyPage(webapp2.RequestHandler):
    def get(self):
       # about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write("This is the survey page")
        
class ResultsPage(webapp2.RequestHandler):
    def get(self):
        #about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write("This is the results page")        



app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/login', LoginPage),
    ('/survey', SurveyPage),
    ('/results', ResultsPage),
], debug=True)