
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
    user.uid = request['uid']
    user.fingerprint = request['fpr']
    user.put()
    response.write('Added %s successfully' % user.fingerprint)

  elif(method == 'getfriends'):
    users = SocialUser.all()
    for user in users:
      response.write(user.uid + ',')
  elif(method == 'getfprs'):
    users = SocialUser.all()
    for user in users:
      response.write(user.fingerprint + ',')
  else:
    response.write('Call %s not support' % method)

  return response
