import socket, logging, threading, os, urllib.parse
from datetime import datetime, timezone
# Comment out the line below to not print the INFO messages
logging.basicConfig(level=logging.INFO)


class HttpRequest():
    def __init__(self, requeststr):
        self.rstr = requeststr
        self.rjson = {}
        self.parse_string()


    def parse_string(self):
        #break the string into the tokens
        if self.rstr is not '':
            splitstring = self.rstr.split('\r\n')
            request_line = splitstring[0].split( )
            i = 1
            header_values = []
            header_fields = []
            body = []
            self.rjson = {'request-line': {
                'method': request_line[0],
                'URI': request_line[1],
                'version': request_line[2]
            }, 'headers': [], 'body':''}

            for string in splitstring[1:-1]:
                if string != '':
                    temp = string.split(':', 1)
                    self.rjson['headers'].append({temp[0]:temp[1].strip()})

            print(self.rstr)
            self.rjson['body'] = splitstring[-1]


    def display_request(self):
        print(self.rjson)

    def getLMT(self,path):
        last_mod_time = ''
        if path is not '':
            last_mod_time = os.path.getmtime(path)
        else:
            last_mod_time = datetime.utcnow().timestamp()
        last_mod_time = datetime.fromtimestamp(last_mod_time)
        last_mod_string = f'{last_mod_time.strftime("%A")[:3]}, {last_mod_time.day} {last_mod_time.month} {last_mod_time.year}  {last_mod_time.hour}:{last_mod_time.minute}:{last_mod_time.second} GMT'
        return last_mod_string

    def process_packet(self):
        string = ''
        if self.rjson['request-line']['method'] == 'POST':
            temp_body_start = '<html>\n\n<body>\n\t'
            temp_body_end = '</body>\n\n</html>'
            response_body = urllib.parse.unquote_plus(self.rjson['body'])
            response_body = response_body.split('&')
            for element in response_body:
                element = element.split('=')
                temp_body_start = temp_body_start + f'<h1>{element[0]}: {element[1]}</h1>\n'
            body = temp_body_start + temp_body_end
            content_length = len(body)
            last_mod_time = self.getLMT('')
            string = f"HTTP/1.1 200 OK\r\nContent-length {content_length}\r\nServer: cihttpd\r\nLast-modified {last_mod_time}\r\n\r\n{body}"
        if self.rjson['request-line']['method'] == 'GET' or self.rjson['request-line']['method'] == 'HEAD':
            if self.rjson['request-line']['URI'] != '/':
                try:
                    path = self.rjson['request-line']['URI']
                    if not path[1:].startswith('www'):
                        path = '/www' + path
                    html_file = open(path[1:]).read()
                    content_length = len(html_file)
                    last_mod_time = self.getLMT(path[1:])
                    string = f"HTTP/1.1 200 OK\r\nContent-length {content_length}\r\nServer: cihttpd\r\nLast-modified {last_mod_time}\r\n\r\n"
                    if self.rjson['request-line']['method'] == 'GET':
                        string = string + html_file
                except:
                    string = "HTTP/1.1 404\r\nServer: cihttpd\r\n\r\n<html><body><h1>404</h1><p>File Not Found</p></body></html>"
            else:
                string = "HTTP/1.1 200 OK.\r\nServer: cihttpd\r\n\r\n<html><body><p>Welp, NOT a Garbage Tier Server.</p></body></html>"
        return string

class ClientThread(threading.Thread):
    def __init__(self, address, socket):
        threading.Thread.__init__(self)
        self.csock = socket
        logging.info('New connection added.')
        self.httpreq = []


    def run(self):
        # exchange messages
        request = self.csock.recv(1024)
        req = request.decode('utf-8')
        logging.info('Recieved a request from client: ' + req)
        self.httpreq = HttpRequest(req)
        if req != '':
            #self.csock.send(b"HTTP/1.1 500 Not a real fake server (yet).\r\nServer: cihttpd\r\n\r\n<html><body><h1>500 Internal Server Error</h1><p>Garbage Tier Server.</p></body></html>")


            self.httpreq.display_request()


            # send a response
            response = self.httpreq.process_packet().encode('utf-8')
            if response != '':
                self.csock.send(response)

        # disconnect client
        self.csock.close()
        logging.info('Disconnect client.')


def server():
    logging.info('Starting cihttpd...')

    # start serving (listening for clients)
    port = 9001
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost',port))

    while True:
        sock.listen(1)
        logging.info('Server is listening on port ' + str(port))

        # client has connected
        sc,sockname = sock.accept()
        logging.info('Accepted connection.')
        t = ClientThread(sockname, sc)
        t.start()


server()