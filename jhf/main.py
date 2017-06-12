#!/usr/bin/env python

import cgi
import webapp2
import json
import logging

class MainPage(webapp2.RequestHandler):
  # def __init__(self):
    #items = [] 
    #response = { }
    #self.request.url = 'https://api.api.ai/v1/query?v=20150910'
    # def dispatch(self):
    #   self.response.headers['Access-Control-Allow-Origin'] = '*'
    #   super(MainPage, self).dispatch()

    self.request.method = 'POST'
    # #self.request.headers['Authorization'] = 'Bearer ' + 0193cf9c63c14b3188633ea7315deb91, ['Content-Type'] = 'application/json; charset=utf-8'
    self.request.body
    #items.append({'query': query})
    #response['userInformation'] = items
    #return response #return json data

    # def post(self):
    #     self.response.headers['Access-Control-Allow-Origin'] = '*'
    #     self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        
    #     logging.info(self.request)
    #     self.response.out.write('Hello, webapp2 World!')


app = webapp2.WSGIApplication([
  ('/no', MainPage)
], debug=True)


# def main():
#     run_wsgi_app(app)

# if __name__ == "__main__":
#     main()
