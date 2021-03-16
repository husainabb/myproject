# from app import db, Games

# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(30), nullable=False)
#     last_name = db.Column(db.String(30), nullable=False)
#     cars=db.relationship("Cars", backref="person")

# class Cars(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     make = db.Column(db.String(30), nullable=False)
#     model = db.Column(db.String(30), nullable=False)
#     year = db.Column(db.Date, nullable=False)
#     person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=False)

# class Enrolments(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     class_id = db.Column('classes_id', db.Integer, db.ForeignKey('classes.id'))
#     student_id = db.Column('student_id', db.Integer, db.ForeignKey('students.id'))
#     enrollment_date = db.Column('Date', db.String(30))


# class Students(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(30), nullable=False)
#     last_name = db.Column(db.String(30), nullable=False)
#     enrolments = db.relationship('Enrolments', backref='students')

# class Classes(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     subject = db.Column(db.String(30), nullable=False)
#     enrolments = db.relationship('Enrolments', backref='class')


# class Orders(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     fk_user_id=db.Column(db.Integer, nullable=False)
#     order_date=db.Column(db.Date, nullable=False)

# db.drop_all()
# db.create_all()


# # person_insert=Person(first_name="robert", last_name="lewis")
# # db.session.add(person_insert)

# # person_delete=db.session.get(2)
# # db.session.person_delete(person_delete)

# db.session.commit()

from app import db, Games

db.create_all()

first_game=Games(name="man utd vs man city")
second_game=Games(name="Chelsea vs man city")
third_game=Games(name="Arsenal vs man city")

db.session.add(first_game)
db.session.add(second_game)
db.session.add(third_game)
db.session.commit()