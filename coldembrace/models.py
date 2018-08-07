from google.appengine.ext import ndb

class Userdata(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    birth_year = ndb.StringProperty(required=True)
    death_year = ndb.StringProperty(required=True)
    user_sex = ndb.StringProperty(required=True)