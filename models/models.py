from application import db

class StudentsModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    contactNumber = db.Column(db.Integer())
    emailId = db.Column(db.String())

    def __init__(self, name, contact_number, email_id):
        self.name = name
        self.contactNumber = contact_number
        self.emailId = email_id

    def __repr__(self):
        return f"<Student {self.name}>"