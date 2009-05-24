import cgi

from django.http import HttpResponse, HttpResponseRedirect
from models import SocialUser

from google.appengine.ext import db

def test(request):
  return HttpResponse('hello world1')

def api(request):
  response = HttpResponse()

  try:
    method = request['m']
  except:
    method = 'None'

  if(method == 'store'):
    user = SocialUser()
    user.uid = cgi.escape(request['uid'])
    user.fingerprint = cgi.escape(request['fpr'])
    user.put()
    response.write('Added %s successfully' % user.fingerprint)

  elif(method == 'getfriends'):
    users = db.GqlQuery("SELECT * FROM SocialUser ORDER BY date")
    for user in users:
      response.write(user.uid + '\n')
  elif(method == 'getfprs'):
    users = db.GqlQuery("SELECT * FROM SocialUser ORDER BY date")
    for user in users:
      response.write(user.fingerprint + '\n')
  else:
    response.write('Call %s not support' % method)

  return response
