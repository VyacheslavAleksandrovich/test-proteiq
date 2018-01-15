from google.appengine.ext import ndb

class InputFileCSV(ndb.Model):
    content = ndb.TextProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

class OutFileCSV(ndb.Model):
    content = ndb.TextProperty()
    uuid = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
