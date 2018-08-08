from google.appengine.ext import ndb

<<<<<<< HEAD
class current_user(ndb.Model):
    line1 = ndb.StringProperty(required=True)
    line2 = ndb.StringProperty(required=True)
    line3 = ndb.StringProperty(required=True)
    line4 = ndb.StringProperty(required=True)
    line5 = ndb.StringProperty(required=True)
    line6 = ndb.StringProperty(required=True)
    line7 = ndb.StringProperty(required=True)
    
class other_user1(ndb.Model):
    line8 = ndb.StringProperty(required=True)
    line9 = ndb.StringProperty(required=True)
    
class other_user2(ndb.Model):
    line8 = ndb.StringProperty(required=True)
    line9 = ndb.StringProperty(required=True)

class other_user3(ndb.Model):
    line8 = ndb.StringProperty(required=True)
    line9 = ndb.StringProperty(required=True)
    
class other_user4(ndb.Model):
    line8 = ndb.StringProperty(required=True)
    line9 = ndb.StringProperty(required=True)
    
class other_user5(ndb.Model):
    line8 = ndb.StringProperty(required=True)
    line9 = ndb.StringProperty(required=True)

class other_user6(ndb.Model):
    line8 = ndb.StringProperty(required=True)
    line9 = ndb.StringProperty(required=True)
    
class other_user7(ndb.Model):
    line8 = ndb.StringProperty(required=True)
    line9 = ndb.StringProperty(required=True)
=======
class Userdata(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    birth_year = ndb.StringProperty(required=True)
    death_year = ndb.StringProperty(required=True)
    user_sex = ndb.StringProperty(required=True)
>>>>>>> 0ed3c7e97c42ac4b882284e3f60df6b9f7c28215
