import cgi
import csv

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
        <html>
            <body>
                <form action="/numbers" class="form-horizontal" enctype="multipart/form-data" method="post">
                    <div><input multiple id="file" name="attachments" type="file"></div>
                    <div><input type="submit"></div>
                </form>
            </body>
        </html>""")

class FileProcessor(webapp2.RequestHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'text/csv'
        self.response.headers['Content-Disposition'] = 'attachment; filename=process_numbers.csv'
        writer = csv.writer(self.response.out)
        writer.writerow(['Num'])
        #print('file obj: ', self.request.POST.multi['attachments'].file)
        #with self.request.POST.multi['attachments'].file as csv_file:
        for line in self.request.POST.multi['attachments'].file.read().split()[1:]:
            writer.writerow([line])
        return redirect('/')
                
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/numbers', FileProcessor)
], debug=True)

def main():
    application.run()
    

if __name__ == '__main__':
    main()
