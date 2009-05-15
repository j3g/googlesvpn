import cgi

from django.http import HttpResponse, HttpResponseRedirect
from models import SocialUser

from google.appengine.ext import db

def test(request):
  return HttpResponse('hello world1')

def api(request):
  response = HttpResponse()

  method = request.GET['m']

  if(method == 'store'):
    user = SocialUser()
    user.uid = cgi.escape(request.GET['uid'])
    user.fingerprint = cgi.escape(request.GET['fpr'])
    user.put()
    response.write('Fingerprint %s add' % user.fingerprint)

  elif(method == 'getfriends'):
    users = db.GqlQuery("SELECT * FROM SocialUser ORDER BY date")
    for user in users:
      response.write(user.uid)
  elif(method == 'getfprs'):
    users = db.GqlQuery("SELECT * FROM SocialUser ORDER BY date")
    for user in users:
      response.write(user.fingerprint)
  else:
    response.write('Call %s not support' % method)

  return response
