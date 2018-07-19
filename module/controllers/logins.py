from flask import render_template, redirect
from module.config.mysqlconnection import connectToMySQL
from module.models.login import Login

login = Login()


mysql = connectToMySQL('lognreg')

print("all users", )

class Logins():
    def index(self):
        result1 = login.index()
        return render_template("index.html")
    

    def register(self):
        result2 = login.register()
        return redirect('/success')


    def login(self):
        result3 = login.login()
        return redirect('/success')

    def logout(self):
        result4 = login.logout()
        return redirect('/')


    def success(self):
        result5 = login.success()
        return render_template('success.html', name = result5)
