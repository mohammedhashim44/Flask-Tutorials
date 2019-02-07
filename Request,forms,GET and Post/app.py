
# Import the flask module 
from flask import Flask , request

# Initiate the app 
app = Flask(__name__) 

@app.route('/')
def index():
    return "Hello World"

@app.route('/getForm')
def getForm():
    return """ 
            <form action="/processGet" method="GET" >
                <input type="text" name="name" >
                <input type="submit" >
            <form>
            """

@app.route('/processGet')
def processGet():
    name = request.args.get('name' , default=None) 
    return str(name)

@app.route('/postForm')
def postForm():
    return """ 
            <form action="/processPost" method="POST" >
                <input type="text" name="name" >
                <input type="submit" >
            <form>
            """

# Method not allowed 
@app.route('/processPost' , methods=['GET','POST'])
def processPost():
    name = request.form.get('name' , default=None) 
    return str(name)



app.run()