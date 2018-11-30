import datetime
import sys

from bottle import *
from peewee import fn

sys.path.append('../')
#from  bottle import get,static_file,route,template,run,request
from Site.models import Logs



@get("<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")
@get("<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

@get('/newdata')
def adddata():
    lo=Logs(h=request.GET.get('h'),
            t=request.GET.get('t'),
            ah=request.GET.get('ah'),
            at=request.GET.get('at'),
            l=request.GET.get('l'),
            date=datetime.datetime.now())
    lo.save()


@route('/')
def index():
    logs=Logs.select().where( max(Logs.id) )

    return template('index.html',logs=logs)


#host='0.0.0.0'
run(port=7000)
