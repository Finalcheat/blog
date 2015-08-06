#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tornado.ioloop
import tornado.web
import motor

def getMongoDBClient():
    return motor.MotorClient()

class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def post(self):
        print("git pull start")
        os.system("cd /root/blog")
        os.system("git pull origin master &")
        print("git pull finish")
        headers = self.request.headers
        body = self.request.body
        mongo = getMongoDBClient()
        yield mongo.bitbucket.record.insert(headers)
        yield mongo.bitbucket.record.insert(body)
        self.write("Hello, world")


application = tornado.web.Application([
    (r"/git_pull_code_auth_is_007/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
