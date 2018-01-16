from google.appengine.ext import ndb
import webapp2

from lib.entity import InputFileCSV, OutFileCSV
from time import sleep

class ProcessFile(webapp2.RequestHandler):
    def post(self):
        urlkey = self.request.get('urlkey')
        s_k = self.request.get('uuid')
        file_key = ndb.Key(urlsafe=urlkey)
        csv_file = file_key.get()
        result_file = OutFileCSV(content=csv_file.content,
                                 uuid=s_k)
        sleep(3)
        print('sleep is done')
        result_file.put()


application = webapp2.WSGIApplication([
    ('/process_file', ProcessFile)
], debug=True)
