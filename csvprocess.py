import csv

import webapp2

from primes.prime import get_all_prime_to_num, get_two_opts

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
        #primes = get_all_prime_to_num(999)
        writer = csv.writer(self.response.out)
        writer.writerow(['Num'])
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
