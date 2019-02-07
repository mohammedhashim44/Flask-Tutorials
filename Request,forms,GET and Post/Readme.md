# Tutorial 2 : Requests,forms,GET and POST

## How to setup : 

- If the last example is working this will work

## The examble :

In the last example we made an app that just print "Hello World" , that's not very interresting right ?

Today we will learn one of the fundemental web concepts : POST and GET

So, what happend when you run the last example? you entered the URL "localhost:5000", then Hello World string showed app 

This is call request and response, You entering the URL is a reuest to the server, you are asking it something , and the "Hello World" is response from the server 

In the request we have 2 types : GET and POST 

These called request methods, used for tranferring data from page to another.

Let's talk about GET, when you open google it's something like this 'www.google.com' , when you search it becomes something like this 'www.google.com/search?q=YourSearchString' 

The word you earched in first page transfered to the another page with the URL 

But if it was using post it will be like this 'www.google.com/search' 

So , in GET the data sent with the URL paramaetars like this , `www.example.com/page?name=Name&email=Email .. etc`
And in POST it just sent with the request itself without showing in the URL `www.example.com/page' 


GET : The data transfer throw the URL  
Pros : It simple  
Cons : It is very bad for sensative data, if the data is too long the URL can't handle it, the webpage with the URL can be saved  

POST : The data tranfer with the request it self , the data are protected 

### So, just use POST if the data is to long , or you are submitting a form with sensative data.Otherwise use GET.

Let's see the examle , In HTMl the form is like this 

```html
<form method="" action="" >
  <input name="name" type="text" >
  <input type="submit" >
</form>
```

The action is page wich the data will be send to when the form is submitted.
The method is GET or POST , if it's now written the defualt is GET 

Let's see the example , first we import the `request` from flask

This is the simplest app you can build with flask 

```python
from flask import Flask , request
``` 

Next we define the method 

```python
@app.route('/getForm')
def getForm():
    return """ 
            <form action="/processGet" method="GET" >
                <input type="text" name="name" >
                <input type="submit" >
            <form>
            """
``` 

This method just return HTML form , the method is get and the data will tranfered to '/processGet'

Next 

```python
@app.route('/processGet')
def processGet():
    name = request.args.get('name' , default=None) 
    return str(name)
```

This page will is where the processing happends , the data from 'getForm' will be sent like this in URL :

localhost:5000/processGet?name=YOURNAME 

Now to get this data from the URL , you will use

```python
name = request.args.get('o' , default=None)
```

If there is no argument with the name "name" the default is "None" 

------------------------

Now for the other method 

```python
@app.route('/postForm')
def postForm()
```
and 
```python
@app.route('/processPost' , methods=['GET','POST'])
def processPost():
```

It's just the same , the diffrence it that the second form has 'post' method , and the action is '/processPost'

To get the argument use 
```python
name = request.form.get('name' , default=None) 
```

-----------------------

For Get you use `request.args.get` , and with post you use `request.form.get` :)


