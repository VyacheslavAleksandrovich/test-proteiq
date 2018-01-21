from google.appengine.ext import ndb
from google.appengine.api import urlfetch
import webapp2

from lib.entity import InputFileCSV, OutFileCSV
from time import sleep
from collections import deque
from functools import partial
import json
import csv
from StringIO import StringIO

SERVICE_QUERY = 'https://primesinfo-192413.appspot.com/?num='

def append_result(q, rpc):
    result = rpc.get_result()
    if result.status_code == 200:
        q.append(result.content)

class ProcessFile(webapp2.RequestHandler):
    def post(self):
        urlkey = self.request.get('urlkey')
        s_k = self.request.get('uuid')
        input_file_key = ndb.Key(urlsafe=urlkey)
        csv_file = input_file_key.get()
        result_queue = deque()
        rpcs = deque()
        string_buffer = StringIO()
        csv_writer = csv.writer(string_buffer)
        csv_writer.writerow(['Number', 'Prime', 'Option_1', 'Option_2', 'ProcessingTime'])
        for num in csv_file.content.split()[1:]:
            rpc = urlfetch.create_rpc(deadline=5)
            append_result_q = partial(append_result, result_queue, rpc)
            rpc.callback = append_result_q
            urlfetch.make_fetch_call(rpc, SERVICE_QUERY+num)
            rpcs.append(rpc)
        for rpc in rpcs:
            rpc.wait()
        for res in result_queue:
            rdict = json.loads(res)
            csv_writer.writerow(map(str, [rdict['number'], rdict['prime'], 
                                          rdict['Option_1'], rdict['Option_2'], 
                                          rdict['processing_time']]))
        result_file_key = OutFileCSV(content=string_buffer.getvalue(), uuid=s_k)
        result_file_key.put()
        input_file_key.delete()


application = webapp2.WSGIApplication([
    ('/process_file', ProcessFile)
], debug=True)
