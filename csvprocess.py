import uuid

from google.appengine.ext import ndb
from google.appengine.api import taskqueue
import webapp2
from webapp2_extras import sessions

#from lib.prime import get_all_prime_to_num, get_two_opts
from lib.entity import InputFileCSV

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        self.session_store = sessions.get_store(request=self.request)
        try:
            webapp2.RequestHandler.dispatch(self)
        finally:
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        return self.session_store.get_session()

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
        <html>
            <body>
                <form action="/upload_file" class="form-horizontal" enctype="multipart/form-data" method="post">
                    <div><input multiple id="file" name="attachments" type="file"></div>
                    <div><input type="submit"></div>
                </form>
            </body>
        </html>""")

class FileFormHandler(BaseHandler):
    def post(self):
        #self.response.headers['Content-Type'] = 'text/csv'
        #self.response.headers['Content-Disposition'] = 'attachment; filename=process_numbers.csv'
        #primes = get_all_prime_to_num(999)
        #writer = csv.writer(self.response.out)
        #writer.writerow(['Num'])
        #for line in self.request.POST.multi['attachments'].file.read().split()[1:]:
        #    writer.writerow([line])
        #return redirect('/')
        result_id = str(uuid.uuid1().int)
        self.session['result_id'] = result_id
        content = self.request.POST.multi['attachments'].file.read()
        input_file = InputFileCSV(content=content)
        key = input_file.put()
        task = taskqueue.add(
                url='/process_file',
                target='worker',
                params={'uuid': result_id, 'urlkey': key.urlsafe()})

        
config = {}
config['webapp2_extras.sessions'] = {'secret_key': 'super_secret_key',}
                
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/upload_file', FileFormHandler)
], debug=True, config=config)

def main():
    application.run()
    

if __name__ == '__main__':
    main()
