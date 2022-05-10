from flask import Flask,request,render_template
from controller.main_controllers import *



app=Flask(__name__)


if __name__=="__main__":
    app.run(debug=True)