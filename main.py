from bottle import route, run, template, request
import pymysql
from connector import connector as con

@route('/')
def index():
    data = con()
    return template('template.html', 
                    result=data.lastTen()
           )

@route('/searchByName', method='POST')
def searchByName():
    name = request.forms.get('name')
    name = name.encode('latin1')
    name = name.decode('utf-8')
    data = con()
    return template('template.html', 
                    result=data.searchByName(name)
           )



run(host='localhost', port='8080')