import webapp2
from random import shuffle
import jinja2
import os
from models import Current_user
from models import other_user1

#libraries for APIs
from google.appengine.api import urlfetch
import json
import random


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
def run_query(first_line, second_line, third_line, fourth_line, fifth_line):
    c_user = Current_user(frname = first_line, laname = second_line, birthy = third_line, rebirthy = fourth_line, u_sex = fifth_line)
    current_user_input= c_user.put()
    print("&&&&&&&&&&&&&&&&&&&&&&&&&")
    print current_user_input 

    
class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(home_template.render())
    
class SurveyPage(webapp2.RequestHandler):
    def get(self):
        survey_template = the_jinja_env.get_template('templates/survey.html')
        self.response.write(survey_template.render())

    def post(self):

        user_fname = self.request.get('fname')
        user_lname = self.request.get('lname')
        user_ybirth = self.request.get('ybirth')
        user_rebirth = self.request.get('yrebirth')
        user_sex = self.request.get('u_sex')
        
        #running query to database
        run_query(user_fname, user_lname, user_ybirth, user_rebirth, user_sex)
        
        #user info in database (entries)
        the_variable_dict = {
            'frname' : user_fname,
            'laname' : user_lname,
            'birthy' : user_ybirth,
            'rebirthy' : user_rebirth,
            'sex' : user_sex,
        }
        #redirecting to results page
        survey_template = the_jinja_env.get_template('templates/results.html')

        self.response.write(survey_template.render(the_variable_dict))

        
class ResultsPage(webapp2.RequestHandler):
    def post(self):
        survey_template = the_jinja_env.get_template('templates/results.html')
        #getting api info and dictionaries for names
        name_generator_url = "https://www.behindthename.com/api/random.json?number=6&randomsurname=yes&key=da143179294"
        randomName= urlfetch.fetch(name_generator_url).content
        names_as_json = json.loads(randomName)
        name = names_as_json['names']
        print "************"
        print name
        
        #name values being grabbed
        the_variable_dict = {
            'options': name
        }
    
        
        #putting names to page
        results_template = the_jinja_env.get_template("templates/match.html")
        self.response.write(results_template.render(the_variable_dict))
        
class MatchPage(webapp2.RequestHandler):
    def get(self):
        match_template = the_jinja_env.get_template('templates/match.html')
        #run_query(frname, laname, birthy, rebirthy, u_sex)
        choice = self.request.get('sex')
        the_variable_dict = {
            "preference":choice
        }
        self.response.write(match_template.render(the_variable_dict))



app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/survey', SurveyPage),
    ('/results', ResultsPage),
    ('/match', MatchPage),
], debug=True)
