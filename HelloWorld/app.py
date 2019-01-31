
# Import the flask module 
from flask import Flask 

# Initiate the app 
app = Flask(__name__) 

@app.route('/')
def index():
    return "Hello World" 

app.run()