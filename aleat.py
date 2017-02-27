#! /usr/bin/python3
from webapp import webApp
import random


class randApp(webApp):
    # We will change parse and process methods
    def parse(self, request):
        return None
        # We don't need to parse, we will only send
        # the socket a new random number as a link

    def process(self, parsedRequest):

        newOne = random.randint(0, 10000)
        code = ('<html><head>' +
                '<a href="http://localhost:1234/' +
                str(newOne) +
                '">Dame otra</a>' +
                '</head></html>')
        return ('200 OK', code)

if __name__ == '__main__':
    randWebApp = randApp('localhost', 1234)
