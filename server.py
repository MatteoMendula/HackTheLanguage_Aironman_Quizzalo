from http.server import BaseHTTPRequestHandler, HTTPServer
from expertai.nlapi.cloud.client import ExpertAiClient
from json import dumps, loads
import os


os.environ["EAI_USERNAME"] = "mattemendu@gmail.com"
os.environ["EAI_PASSWORD"] = "dF4d_?!1x!"

""" The HTTP request handler """
class RequestHandler(BaseHTTPRequestHandler):

  def _send_cors_headers(self):
      """ Sets headers required for CORS """
      self.send_header("Access-Control-Allow-Origin", "*")
      self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
      self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")

  def send_dict_response(self, d):
      """ Sends a dictionary (JSON) back to the client """
      self.wfile.write(bytes(dumps(d), "utf8"))

  def do_OPTIONS(self):
      self.send_response(200)
      self._send_cors_headers()
      self.end_headers()

  def do_GET(self):
      self.send_response(200)
      self._send_cors_headers()
      self.end_headers()

      response = {}
      response["status"] = "OK"
      self.send_dict_response(response)

  def do_POST(self):
    self.send_response(200)
    self._send_cors_headers()
    self.send_header("Content-Type", "application/json")
    self.end_headers()

    dataLength = int(self.headers["Content-Length"])
    data = self.rfile.read(dataLength)

    parsed_data = loads(data)["value"]

    client = ExpertAiClient()

    # text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half."
    text = parsed_data
    language= 'en'

    output = client.full_analysis(body={"document": {"text": text}}, params={'language': language, 'resource': 'entities'})

    print("knowledge: ", output.knowledge)
    print("paragraphs: ", len(output.paragraphs))
    print("sentences: ", len(output.sentences))
    print("phrases: ", len(output.phrases))
    print("tokens: ", len(output.tokens))
    print("mainSentences: ", len(output.main_sentences))
    print("mainPhrases: ", len(output.main_phrases))
    print("mainLemmas: ", len(output.main_lemmas))
    print("mainSyncons: ", len(output.main_syncons))
    print("topics: ", len(output.topics))
    print("entities: ", len(output.entities))
    print("entities: ", len(output.relations))
    print("sentiment.items: ", len(output.sentiment.items))

    for entity in output.entities:
        print (f'{entity.lemma:{50}} {entity.type_:{10}}')


    response = {}
    response["status"] = "OK"
    response["paragraphs"] = len(output.paragraphs)
    response["phrases"] = len(output.phrases)
    response["tokens"] = len(output.tokens)
    response["mainSentences"] = len(output.main_sentences)
    response["mainPhrases"] = len(output.main_phrases)
    response["topics"] = len(output.topics)
    response["entities"] = len(output.entities)

    self.send_dict_response(response)


print("Starting server")
httpd = HTTPServer(("localhost", 8000), RequestHandler)
print("Hosting server on port 8000")
httpd.serve_forever()