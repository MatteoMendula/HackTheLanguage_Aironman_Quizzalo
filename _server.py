# import requests

# url = 'https://www.w3schools.com/python/demopage.php'
# myobj = {'somekey': 'somevalue'}

# x = requests.post(url, data = myobj)

# print(x)
# print("asd")

# Python 3 server example
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from expertai.nlapi.cloud.client import ExpertAiClient

os.environ["EAI_USERNAME"] = "mattemendu@gmail.com"
os.environ["EAI_PASSWORD"] = "dF4d_?!1x!"

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        return super(MyServer, self).end_headers()

    # def end_headers (self):
    #     self.send_header('Access-Control-Allow-Origin', '*')
    #     self.end_headers()

    # def do_OPTIONS(self):
    #     self.send_response(200, "ok")
    #     self.send_header('Access-Control-Allow-Origin', '*')
    #     self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    #     self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
    #     self.send_header("Access-Control-Allow-Headers", "Content-Type")
    #     self.end_headers()
        
    def do_GET(self):
        self.send_response(200, "ok")
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200, "ok")
        self.send_header('Content-Type', 'application/json')
        
        # self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        json_str = json.dumps({'hello': 'world', 'received': 'ok'})
        # client = ExpertAiClient()

        # text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half."
        # language= 'en'

        # output = client.specific_resource_analysis(body={"document": {"text": text}}, params={'language': language, 'resource': 'entities'})

        # print (f'{"ENTITY":{50}} {"TYPE":{10}}')
        # print (f'{"------":{50}} {"----":{10}}')

        # for entity in output.entities:
        #     print (f'{entity.lemma:{50}} {entity.type_:{10}}')
        self.wfile.write(bytes(json_str, "utf-8"))
        # self.wfile.write(json_str.encode(encoding='utf_8'))
        # self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))
        # self.wfile.write(bytes("<html><body><h1>POST Request Received!</h1></body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")