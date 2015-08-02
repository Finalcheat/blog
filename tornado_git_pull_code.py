#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        print("git pull start")
        os.system("cd /root/blog")
        os.system("git pull origin master &")
        print("git pull finish")
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/git_pull_code_auth_is_007/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
