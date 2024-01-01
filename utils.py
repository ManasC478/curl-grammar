import uuid

def method_has_path(request_data):
    if request_data['method'] == 'GET':
        return True
    elif request_data['method'] == 'POST':
        if request_data['path_base'] == 'student' and not request_data['path_student_id']:
            return True
        return False
    elif request_data['method'] == 'PATCH':
        if request_data['path_base'] == 'student' and request_data['path_student_id']:
            return True
        return False
    elif request_data['method'] == 'DELETE':
        if request_data['path_base'] == 'student':
            return True
        return False
    
    return False    
    
def validate_data_fields(data):
    valid_keys = set(['name','email', 'age','year','bio', 'major','university', 'links'])
    
    for key in data.keys():
        if key not in valid_keys:
            return False
    
    return True

def validate_post_data_fields(data):    
    if 'name' not in data or 'email' not in data:
        return False
    
    return validate_data_fields(data)
    
def validate_data_types(data):
    type_contraints = {'name': str, 'email': str, 'age': int, 'bio': str, 'year': str, 'major': str, 'university': str, 'links': list}
    
    for key in data.keys():
        if type(data[key]) != type_contraints[key]:
            return False
        
    return True

def validate_data_values(students, data):
    if 'email' in data:
        for student in students:
            if data['email'] == student['email']:
                return False

    if 'age' in data and (data['age'] < 18 or data['age'] > 22):
        return False

    if 'year' in data and data['year'] != 'Freshman' and data['year'] != 'Sophomore' and data['year'] != 'Junior' and data['year'] != 'Senior':
        return False

    return True

def create_new_student(data):
    new_student = {'id': str(uuid.uuid4()), 'age': None, 'bio': None, 'year': 'Freshman', 'major': None, 'university': None, 'links': []}
 
    new_student.update(data)
    
    return new_student