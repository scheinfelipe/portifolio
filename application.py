from flask import Flask

application = Flask(__name__)
application.config.from_object('config.Dev')

from views import *

if __name__ == '__main__':
    application.run()
