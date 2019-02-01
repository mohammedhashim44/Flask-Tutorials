# Tutorial 1 

## How to setup : 

- Make sure you have python3 
- Make sure you have 'pip' installed 
- Install flask module by this command `pip3 install Flask` , or 'pip' depend on your system

## The examble :

This is the simplest app you can build with flask 

```python
from flask import Flask 

app = Flask(__name__) 
``` 

You import the module, create new app , the you define the routes .

```python
@app.route('/')
def index():
  return "Hello World" 
```

This code means whenever the user go to the path '/', the function will 'index' will be called .
When 'index' called , it will just return "Hello World" string to the browser .

Last thing we run the app 
```python
app.run() 
```

To run the program , type :

`python3 app.py`

This will open a server, then you go to the browser and eneter the URL :
http://localhost:5000/ 


If everything is right , you should see "Hello World" in the broswer .

Thats all for today :) 
