from flask import Flask, flash, render_template, redirect, session, Session, request, abort, send_from_directory
from cbtpackage import app, db
from cbtpackage.model import *
from cbtpackage.form import *
from werkzeug import secure_filename
import os


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        password= request.form['password']

        query = db.session.query(Users).filter(Users.email==email, Users.password==password).first()
        if query:
            session['uname'] = query.firstname 
            session['email'] = query.email
            session['usertype'] = query.usertype
            if query.usertype == 'admin':
                return 'admin'
            else:
                return 'user'
            
        else: 
            return 'failed'
    else:
        return render_template('login.html')

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password= request.form['password']

        query = Users(firstname=firstname, lastname=lastname, email=email, password=password, usertype="user")
        db.session.add(query)
        db.session.commit()
        if query.id:
            alert_ = 'You have been registered successfully'
        else:
            alert_ = 'An error occured'
        flash(alert_)
        return redirect('/register')
    else:
        return render_template('register.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot-password.html')


@app.route("/admin/library", methods=['POST','GET'])
def library():
     if session.get('uname') :
          if session.get('usertype') == 'admin':
               uname = session.get('uname')
               form2 = AddBooks()
               if form2.validate_on_submit():
                    bookfile = request.files['book_file']
                    book_name_secure = secure_filename(bookfile.filename)
                    bookfile.save('book_uploads/'+book_name_secure)

                    booktitle = request.form['book_title']
                    bookdescription = request.form['book_description']
                    bookauthor = request.form['book_author']
                    bookstatus = request.form['status']
                    query1 = Library(book_title=booktitle, book_description=bookdescription, book_author=bookauthor, book_status=bookstatus, book_file=book_name_secure, active=1)
                    db.session.add(query1)
                    db.session.commit()

                    if query1.id:
                         alert_ = 'Book Succesfully Added'
                    else:
                         alert_ = 'An Error Occurred'
                    flash(alert_)
                    return redirect('/admin/library')
               else:
                    query2 = db.session.query(Library).filter(Library.active==1).all()
                    return render_template('/library1.html', form2=form2, query=query2, uname=uname)
          else:
                abort (404)
     else:
          return redirect('/')

@app.route("/admin/updatelibrary/<id_>", methods=['POST','GET'])
def updatelibrary(id_):
     if session.get('uname') :
          if session.get('usertype') == 'admin':
               uname = session.get('uname')
               form2 = AddBooks()
               if form2.validate_on_submit():
                    if request.files.get('book_file'):
                         bookfile = request.files['book_file']
                         book_name_secure = secure_filename(bookfile.filename)
                         bookfile.save('book_uploads/'+book_name_secure)

                         booktitle = request.form['book_title']
                         bookdescription = request.form['book_description']
                         bookauthor = request.form['book_author']
                         bookstatus = request.form['status']
                         query1 = db.session.query(Library).get(id_)
                         query1.book_title=booktitle
                         query1.book_description=bookdescription
                         query1.book_author=bookauthor
                         query1.book_status=bookstatus
                         query1.book_file=book_name_secure                         
                         db.session.commit()

                         if query1.id:
                              alert_ = 'Book Succesfully Updated'
                         else:
                              alert_ = 'An Error Occurred'
                         flash(alert_)
                         return redirect('/admin/library')
                    else:
                         booktitle = request.form['book_title']
                         bookdescription = request.form['book_description']
                         bookauthor = request.form['book_author']
                         bookstatus = request.form['status']
                         query1 = db.session.query(Library).get(id_)
                         query1.book_title=booktitle
                         query1.book_description=bookdescription
                         query1.book_author=bookauthor
                         query1.book_status=bookstatus                                                  
                         db.session.commit()

                         if query1.id:
                              alert_ = 'Book Succesfully Updated'
                         else:
                              alert_ = 'An Error Occurred'
                         flash(alert_)
                         return redirect('/admin/library')
               else:
                    query2 = db.session.query(Library).filter(Library.id==id_)
                    return render_template('/blank.html', form2=form2, query2=query2, uname=uname)
          else:
                abort (404)
     else:
          return redirect('/')

@app.route("/deletelibrary/<lib_id>")
def deletelibrary(lib_id):
     if session.get('uname') :
          if session.get('usertype') == 'admin':
               query1 = db.session.query(Library).get(lib_id)
               query1.active = 0
               db.session.commit()

               if query1.id:
                    alert_ = 'Book Succesfully Deleted'
               else:
                    alert_ = 'An Error Occurred'
               flash(alert_)
               return redirect('/admin/library')
          else:
                abort (404)
     else:
          return redirect('/')

@app.route("/admin/confirmbookfiletype", methods=["POST","GET"])
def bookfileerror():
     file = request.files['file']
     name,ext = os.path.splitext(file.filename)
     file.save('tmp/'+file.filename)
     size = os.stat('tmp/'+file.filename).st_size
     if ext in ['.pdf','.docx','.doc']:
          if int(size) < 2000000:
               os.remove('tmp/'+file.filename)
               return 'good'
          else:
               os.remove('tmp/'+file.filename)
               return 'sizebad'
     else:
          os.remove('tmp/'+file.filename)
          return 'typebad'

@app.route("/download/<filename>", methods=['GET','POST'])
def downloads(filename):
     if session.get('uname'):
          
            return send_from_directory('../'+app.config['BOOK_FILE_UPLOAD'], filename=filename, as_attachment=True) 
         
     else:
          return redirect('/')

@app.route('/logout')
def logout():
     if session.get('uname'):
          session.pop('uname')
          session.pop('usertype')
         
          return redirect('/')
     else:
          return redirect('/')