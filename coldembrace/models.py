from google.appengine.ext import ndb

<<<<<<< HEAD
class Userdata(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    birth_year = ndb.StringProperty(required=True)
    death_year = ndb.StringProperty(required=True)
    user_sex = ndb.StringProperty(required=True)
=======
class Meme(ndb.Model):
    line1 = ndb.StringProperty(required=True)
    line2 = ndb.StringProperty(required=True)
    img_choice = ndb.StringProperty(required=False)
>>>>>>> 2735cec8363790274892cc82ef20e11a3c87f8f2
