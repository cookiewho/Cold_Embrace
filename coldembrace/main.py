import webapp2
from random import shuffle
import jinja2
import os


#libraries for APIs
from google.appengine.api import urlfetch
import json # Javascript Object Notation


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
#def login_query(user_name, pass_word):
    #userinfo = userinfo(username = user_name, password = pass_word)


class HomePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write("This is the home page")
<<<<<<< HEAD
        
=======
   
>>>>>>> 2735cec8363790274892cc82ef20e11a3c87f8f2
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
        name_generator_url = "https://www.behindthename.com/api/random.json?number=6&randomsurname=yes&key=da143179294"
        randomName= urlfetch.fetch(name_generator_url).content
        nameOfGhost = json.loads(randomName)
        self.response.write(nameOfGhost)
        
        the_variable_dict = {
            "name": nameOfGhost
        }
        survey_template = the_jinja_env.get_template("templates/survey.html")
        self.response.write(survey_template.render(the_variable_dict))
<<<<<<< HEAD
=======


>>>>>>> 2735cec8363790274892cc82ef20e11a3c87f8f2
        
class ResultsPage(webapp2.RequestHandler):
    def get(self):
        #about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write("This is the results page")        



app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/survey', SurveyPage),
    ('/results', ResultsPage),
], debug=True)
