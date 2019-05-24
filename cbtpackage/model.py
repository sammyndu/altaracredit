from cbtpackage import db
from datetime import datetime
from datetime import date

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    firstname= db.Column(db.String(50),nullable=False)
    lastname= db.Column(db.String(50),nullable=False)
    email= db.Column(db.String(50),nullable=False)
    password= db.Column(db.String(100),nullable=False)
    usertype= db.Column(db.String(20),nullable=False)

class ExamSetup(db.Model):
    __tablename__ = 'exam_setup'
    id = db.Column(db.Integer(), primary_key=True)
    exam_title= db.Column(db.String(50),nullable=False)
    exam_description= db.Column(db.String(50),nullable=False)
    exam_duration= db.Column(db.Integer(),nullable=False)
    exam_instructions= db.Column(db.String(100),nullable=False)
    exam_question = db.relationship('ExamQuestion', backref='exam_setup')
    exam_answer = db.relationship('ExamAnswer', backref='exam_setup')

class ExamQuestion(db.Model):
    __tablename__ = 'exam_question'
    id = db.Column(db.Integer(), primary_key=True)
    exam_setup_id = db.Column(db.Integer(), db.ForeignKey('exam_setup.id'), nullable=False)
    exam_question= db.Column(db.String(200),nullable=False)
    exam_option= db.Column(db.String(100),nullable=False)
    exam_option_val= db.Column(db.String(10),nullable=False)
    exam_answer = db.relationship('ExamAnswer', backref='exam_question')

class ExamAnswer(db.Model):
    __tablename__ = 'exam_answer'
    id = db.Column(db.Integer(), primary_key=True)
    exam_setup_id = db.Column(db.Integer(), db.ForeignKey('exam_setup.id'), nullable=False)
    exam_question_id= db.Column(db.Integer(), db.ForeignKey('exam_question.id'), nullable=False)
    exam_answer= db.Column(db.String(100),nullable=False)

class Library(db.Model):
    __tablename__='library'
    id = db.Column(db.Integer(), primary_key=True)
    book_title = db.Column(db.String(50), nullable=False)
    book_description = db.Column(db.String(50), nullable=False)
    book_author = db.Column(db.String(50), nullable=False)
    book_file = db.Column(db.String(50))
    book_status = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Integer(), default=1)





