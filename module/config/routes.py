from module.config.mysqlconnection import connectToMySQL
from module.controllers.logins import Logins
from module import app

logins = Logins()

mysql = connectToMySQL('lognreg')


@app.route("/")
def index():
    return logins.index()

@app.route("/register", methods=['POST'])
def register():
    return logins.register()

@app.route("/login", methods=['POST'])
def login():
    return logins.login()

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return logins.logout()

@app.route("/success")
def success():
    return logins.success()

