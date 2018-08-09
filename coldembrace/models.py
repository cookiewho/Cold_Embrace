from google.appengine.ext import ndb

class current_user(ndb.Model):
    frname = ndb.StringProperty(required=True)
    laname = ndb.StringProperty(required=True)
    birthy = ndb.StringProperty(required=True)
    rebirthy = ndb.StringProperty(required=True)
    u_sex = ndb.StringProperty(required=True)
    
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