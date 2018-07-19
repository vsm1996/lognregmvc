from flask import session, request, flash
from module.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from module import app
import re

app.secret_key = "lolgoodluckbud112210!"
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')





mysql = connectToMySQL('lognreg')


class Login():
    def index(self):
        self.debugHelp("INDEX METHOD")
        return True

    def register(self):
        if len(request.form['first_name']) < 1:
            flash("First name cannot be blank!", 'firstname')
        elif len(request.form['first_name']) <= 2:
            flash("First name must be 2+ characters", 'firstname')
        elif request.form['first_name'].isalpha() == False:
            flash(u"Numbers cannot be in your first name", 'firstname')

        if len(request.form['last_name']) < 1:
            flash("Last name cannot be blank!", 'lastname')
        elif len(request.form['last_name']) <= 2:
            flash("Last name must be 2+ characters", 'lastname')
        elif request.form['last_name'].isalpha() == False:
            flash(u"Numbers cannot be in your last name", 'lastname')
        
        
        query = "SELECT email from user where email = %(email)s"
        
        data = {
            'email': request.form['email']
        }

        email_list = mysql.query_db(query, data)
        print("This is email list: ", len(email_list))
        
        if len(request.form['email']) < 1:
            flash("Email cannot be blank!", 'email')
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!", 'email')
        
        elif len(email_list) > 0:
            flash("That email already exists!", 'email')
        
        
        if len(request.form['password']) < 1:
            flash("Password cannot be blank!", 'password')
        elif len(request.form['password']) < 7:
            flash("Password must be 8 or more characters", 'password')
        
        if len(request.form['pwconfirm']) < 1:
            flash(u"This field is required", 'pwconfirm')
        elif request.form['pwconfirm'] != request.form['password']:
            flash(u"Please make sure both password entries are the same.", 'pwconfirm')
        

        self.debugHelp("REGISTER METHOD")
        if '_flashes' in session.keys():
            return False
        else:
            pw_hash = bcrypt.generate_password_hash(request.form["password"])
            
            flash("You've been successfully registered, ", request.form['first_name'])

            query = "INSERT INTO user (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s,%(email)s, %(password)s, NOW(), NOW());"
                    
            data = {
                'first_name' : request.form['first_name'],
                'last_name' : request.form['last_name'],
                'email' : request.form['email'],
                'password' : pw_hash
            }
            user_info = mysql.query_db(query, data)

            session['logged_in'] = True
            return user_info
        return False
    def login(self):
        query = "SELECT * FROM USER where email = %(email)s"

        data = {
            'email' : request.form['elog']
        }

        email_check = mysql.query_db(query, data)

        print("This is email check: ", email_check)

        if email_check:
            if bcrypt.check_password_hash(email_check[0]['password'], request.form['plog']):
                session['logged_in'] = True
                flash("You successfully logged in...", 'login')
                return True

        session['logged_in'] = False
        flash("Please try again.", 'login')
        
        self.debugHelp("LOGIN METHOD")
        if '_flashes' in session.keys():
            return False
        return False


    def logout(self):
        session['logged_in'] = False
        flash("You have been logged out... ")
        return True

    def success(self):
        if session['logged_in'] == False:
            flash("You are not logged in, please login or register.")
            return False
        return True

    def debugHelp(self, message = ""):
        print("\n\n-----------------------", message, "--------------------")
        print('REQUEST.FORM:', request.form)
        print('SESSION:', session)

