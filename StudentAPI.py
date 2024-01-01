from utils import validate_post_data_fields, validate_data_values, validate_data_types, create_new_student, validate_data_fields
import json

class StudentAPI():
    def __init__(self):
        self.students = []
        self.read_db()
        
    # GET endpoints
    def get_schema(self):
        return {
                'success': True,
                'data': { 'id': 'uuid not null default generate_uuid()', 'name': 'string not null', 'email': 'string not null unique', 'age': 'int min=18 max=22', 'bio':'string', 'year': '“Freshman” | “Sophomore” | “Junior” | “Senior” default “Freshman”', 'major': 'string', 'university': 'string', 'links': 'Array<string> default []::Array<string>' }
                }
                
    def get_students(self):
        return {'success': True, 'data': self.students}
    
    def get_student(self, student_id):
        if not student_id:
            return {'success': False, 'error': 'student_id is null'}
        
        for student in self.students:
            if student['id'] == student_id:
                return {'success': True, 'data': student}
            
        return {'success': True, 'data': None}
    
    # DELETE ENDPOINTS 
    def delete_students(self):
        self.students = []
        self.db_dump()
        return { 'success': True, 'data': [] }
    
    def delete_student(self, student_id):
        if not student_id:
            return {'success': False, 'error': 'student_id is null'}
        
        filtered = list(filter(lambda student: student['id'] != student_id, self.students))
        self.students = filtered
        self.db_dump()
        return {'success': True, 'data': filtered}
        
    # POST ENDPOINTS
    def post_student(self, data):
        if not validate_post_data_fields(data) or not validate_data_types(data) or not validate_data_values(self.students, data):
            return {'success': False, 'error': "Data doesn't follow db constraints"}
        
        new_student = create_new_student(data)
        self.students.append(new_student)
        self.db_dump()
        
        return {'success': True, 'data': new_student}
    
    # PATCH ENDPOINTS
    def patch_student(self, student_id, data):
        if not validate_data_fields(data) or not validate_data_types(data) or not validate_data_values(self.students, data):
            return {'success': False, 'error': "Data doesn't follow db constraints"}
        
        i = 0
        update_student = self.students[i]
        while update_student['id'] != student_id:
            i += 1
            update_student = self.students[i]
            
        update_student.update(data)
        self.db_dump()
        return {'success': True, 'data': update_student}
        
    # DB FILE READ/WRITE
    def db_dump(self):
        json_object = json.dumps(self.students, indent=4)
        
        with open("db.json", "w") as outfile:
            outfile.write(json_object)
            
    def read_db(self):
        with open('db.json', 'r') as json_file:
            self.students = json.load(json_file)