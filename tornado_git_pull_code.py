#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        auth = self.get_argument("auth")
        if auth != "007":
            return self.write("error")
        print "test"
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/git_pull_code/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
