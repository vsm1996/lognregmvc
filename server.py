from module.config.mysqlconnection import connectToMySQL
from module import app
from module.config import routes



mysql = connectToMySQL('lognreg')


if __name__ == "__main__":
    app.run(debug=True)