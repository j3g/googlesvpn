# models.py

from google.appengine.ext import db

class SocialUser(db.Model):
  uid = db.StringProperty()
  fingerprint = db.StringProperty()
  date = db.DateTimeProperty(auto_now_add=True)
