import sys
import test
from wsgi import Application

def run():
    result = test.get(app=Application)
    print (result[ 'status' ], result[ 'headers' ], result[ 'body' ], file=sys.stdout)

run()

