import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class SocialUser(db.Model):
  uid = db.StringProperty()
  fingerprint = db.StringProperty()
  date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, world 3')

class APIHandler(webapp.RequestHandler):
  def get(self):
    method = self.request.get('m')

    self.response.headers['Content-Type'] = 'text/plain'

    if(method == 'store'):
      user = SocialUser()
      user.uid = cgi.escape(self.request.get('uid'))
      user.fingerprint = cgi.escape(self.request.get('fpr'))
      user.put()
      self.response.out.write('Fingerprint %s add' % user.fingerprint)
    elif(method == 'getfriends'):
      users = db.GqlQuery("SELECT * FROM SocialUser ORDER BY date")
      for user in users:
        self.response.out.write(user.uid)
    elif(method == 'getfprs'):
      users = db.GqlQuery("SELECT * FROM SocialUser ORDER BY date")
      for user in users:
        self.response.out.write(user.fingerprint)
    else:
      self.response.out.write('Call %s not support' % method)

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/api', APIHandler),
                                     ], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
