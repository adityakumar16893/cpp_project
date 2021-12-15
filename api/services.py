import json

import models
from application import db
from flask import jsonify, request


class register_services:
    def __init__(self, app):
        self.app = app

        self.app.add_url_rule('/students', '/students', self.students, methods=['POST', 'PUT', 'GET', 'DELETE'])

    def students(self):
        result = {"success": False}

        if request.method == 'POST':
            try:
                data = json.loads(request.data)
                new_student = models.StudentsModel(name=data['name'], contact_number=data['contactNumber'], email_id=data['emailId'])
                db.session.add(new_student)
                db.session.commit()
                result = {"success": True}
            except Exception as e:
                print(e)
                result = {"success": False}
            finally:
                return jsonify(result)
        elif request.method == 'GET':
            results = []
            try:
                students = models.StudentsModel.query.all()
                results = [
                    {
                        "name": student.name,
                        "contactNumber": student.contactNumber,
                        "emailId": student.emailId,
                        "id": student.id
                    } for student in students]
            except Exception as e:
                print(e)
            return jsonify({"students": results})

        elif request.method == 'PUT':
            try:
                data = json.loads(request.data)
                student = models.StudentsModel.query.get_or_404(data['id'])
                if data['name'] and student.name != data['name']:
                    student.name = data['name']
                if data['contactNumber'] and student.contactNumber != data['contactNumber']:
                    student.contactNumber = data['contactNumber']
                if data['emailId'] and student.emailId != data['emailId']:
                    student.emailId = data['emailId']

                db.session.add(student)
                db.session.commit()
                result = {"success": True}
            except Exception as e:
                print(e)
                result = {"success": False}
            finally:
                return jsonify(result)

        elif request.method == 'DELETE':
            try:
                data = json.loads(request.data)
                student = models.StudentsModel.query.get_or_404(data['id'])
                db.session.delete(student)
                db.session.commit()
                result = {"success": True}
            except Exception as e:
                print(e)
                result = {"success": False}
            finally:
                return jsonify(result)
