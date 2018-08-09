import webapp2
from random import shuffle
import jinja2
import os
from models import current_user
from models import other_user1

#libraries for APIs
from google.appengine.api import urlfetch
import json


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
def run_query(first_line, second_line, third_line, fourth_line, fifth_line):
    c_user = current_user(frname = first_line, laname = second_line, birthy = third_line, rebirthy = fourth_line, u_sex = fifth_line)
    current_user_input= c_user.put()
    print("&&&&&&&&&&&&&&&&&&&&&&&&&")
    print current_user_input

    
class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(home_template.render)
        
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
        survey_template = the_jinja_env.get_template('templates/survey.html')
        self.response.write(survey_template.render())
    
    def post(self):
        survey_template = the_jinja_env.get_template('templates/survey.html')
        user_fname = self.request.get('fname')
        user_lname = self.request.get('lname')
        user_ybirth = self.request.get('ybirth')
        user_rebirth = self.request.get('yrebirth')
        user_sex = self.request.get('sex')
        
        run_query(user_fname, user_lname, user_ybirth, user_rebirth, user_sex)
        
        the_variable_dict = {
            'frname' : user_fname,
            'laname' : user_lname,
            'birthy' : user_ybirth,
            'rebirthy' : user_rebirth,
            'u_sex' : user_sex
        }
        self.redirect('/match')

        
class ResultsPage(webapp2.RequestHandler):
    def get(self):
        #about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write("This is the results page")
        
class MatchPage(webapp2.RequestHandler):
    def get(self):
        name_generator_url = "https://www.behindthename.com/api/random.json?number=6&randomsurname=yes&key=da143179294"
        randomName= urlfetch.fetch(name_generator_url).content
        nameOfGhost = json.loads(randomName)
        self.response.write(nameOfGhost)
        
        the_variable_dict = {
            "name": nameOfGhost
        }
        match_template = the_jinja_env.get_template("templates/match.html")
        self.response.write(match_template.render(the_variable_dict))



app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/survey', SurveyPage),
    ('/results', ResultsPage),
    ('/match', MatchPage),
], debug=True)
