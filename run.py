#!flask/bin/python

from app import app
app.run(debug=True) #Stage 1: localhost and clientside debug messages
#app.run(debug=True, host='0.0.0.0') #Stage 2: clientside debug
#app.run() #Stage 3: untested
