from flask import Flask, flash, render_template, redirect, session, Session, request, abort, send_from_directory
from cbtpackage import app, db
from cbtpackage.model import *
from cbtpackage.form import *
from werkzeug import secure_filename
import os

@app.route("/user/library", methods=['POST','GET'])
def user_library():
     if session.get('uname') :
          if session.get('usertype') == 'user':
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
                    return redirect('/user/library')
               else:
                    query2 = db.session.query(Library).filter(Library.active==1).all()
                    return render_template('/library_user.html', form2=form2, query=query2, uname=uname)
          else:
                abort (404)
     else:
          return redirect('/')