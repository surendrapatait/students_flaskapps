from configuration.conf_app import app,request,render_template




@app.route('/home',methods=['POST'])
def student_welcome_page():
    return render_template('home.html')


@app.route('/welcome')
def Student_login_page():
   formdata=request.form

   stid=formdata.get('student_id')
   pas=formdata.get('student_pass')

   if stid.isnumeric() and pas=='Jaihind':
       return render_template('welcome.html',stid)
   else:
       return render_template('home.html',message='INVALID CRENTIALS')

