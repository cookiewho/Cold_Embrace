import webapp2
from random import shuffle
import jinja2
import os
from models import current_user
from models import other_user

#libraries for APIs
from google.appengine.api import urlfetch
import json # Javascript Object Notation


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    def run_query(first_line, second_line, pic_type):
    c_user = current_user(line1=first_line, line2 = second_line, img_choice = pic_type)
    meme_key = meme.put()
    print("&&&&&&&&&&&&&&&&&&&&&&&&&")
    print meme_key

    
class HomePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write("This is the home page")
   
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


        
class ResultsPage(webapp2.RequestHandler):
    def get(self):
        #about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write("This is the results page")        



app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/survey', SurveyPage),
    ('/results', ResultsPage),
], debug=True)
