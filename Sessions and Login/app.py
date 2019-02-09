
# Import the flask module 
from flask import Flask , session , request , render_template , flash , redirect , url_for

# Initiate the app 
app = Flask(__name__) 

# The session can't work without secret key
app.secret_key = "my-secret-key" 

USER = {'username' : 'hello' , 'password':'world'}


@app.route('/')
def index():
    isLogin = False 
    if 'isLogin' in session :
        if session['isLogin'] == True :
            isLogin = True 
    
    return render_template('index.html',isLogin=isLogin)

@app.route('/login' , methods=['GET','POST'])
def login():
    if 'isLogin' in session:
        if session['isLogin'] == True :
            return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form.get('username',default=None)
        password = request.form.get('password',default=None)

        if username == USER["username"] and password == USER["password"]:
            session["isLogin"] = True
            flash("You logged in !")
            return redirect(url_for('index'))
        else:
            flash('Username or password error')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('isLogin' , None) 
    return redirect(url_for('index'))

app.run(debug=True)