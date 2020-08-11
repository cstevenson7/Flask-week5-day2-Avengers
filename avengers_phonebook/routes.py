from avengers_phonebook import app
from flask import render_template, request
#Import the form
from avengers_phonebook.forms import UserInfoForm



#Home page route
@app.route('/')  # decorator
def home():
    
    return render_template("home.html")

#Register route
@app.route('/register', methods= ['GET','POST'])  # decorator
def register():
    form = UserInfoForm()
    #form.validate is checking the CSFR token thing, if the request is a GET it just renders the form
    # if the request == post then the user info entered is SENT
    if request.method == 'POST' and form.validate():
        #Get Information
        username = form.username.data
        password = form.password.data
        email = form.email.data
        phone_number = form.phone_number.data
        print("\n", username,password,email,phone_number)  # this will print out in terminal
    return render_template("register.html", form=form)