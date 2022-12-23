from flask import Flask
from config import vuln_app
import os
from darkspark_python_wsgi import darkspark

app = Flask("__main__")

'''
 Decide if you want to server a vulnerable version or not!
 DO NOTE: some functionalities will still be vulnerable even if the value is set to 0
          as it is a matter of bad practice. Such an example is the debug endpoint.
'''
vuln = int(os.getenv('vulnerable', 1))
# vuln=1
# token alive for how many seconds?
alive = int(os.getenv('tokentimetolive', 600))

vuln_app.app.wsgi_app = darkspark(vuln_app.app.wsgi_app, 'key-2ee36b42dc51e31d61af953c2aaeba546999d739de15ba5c4d225a440f275591')

# start the app with port 2233 and debug on!
if __name__ == '__main__':
    vuln_app.run(host='0.0.0.0', port=2233, debug=True)

