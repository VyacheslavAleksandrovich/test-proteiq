from google.appengine.ext import ndb
import webapp2

from lib.entity import InputFileCSV, OutFileCSV

class ProcessFile(webapp2.RequestHandler):
    def post(self):
        urlkey = self.request.get('urlkey')
        s_k = self.request.get('uuid')
        file_key = ndb.Key(urlsafe=urlkey)
        csv_file = file_key.get()
        result_file = OutFileCSV(content=csv_file.content,
                                 uuid=s_k)
        result_file.put()
        print(result_file)


application = webapp2.WSGIApplication([
    ('/process_file', ProcessFile)
], debug=True)
