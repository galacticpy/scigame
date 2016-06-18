import json

json_file = 'app/data/students_classes.json'

with open(json_file) as data_file:    
    json_data = json.load(data_file)

    #Simple Search Engine
    def search_students(name):
        #Dictionary of matches
        match = {}
        try:
            first = name.split(' ')[0]
            last = name.split(' ', -1)[1]
        except IndexError:
            first = name
            last = name

        #Match Exact
        match['students'] = [student for student in json_data['students'] if first.lower() in student['first'].lower() and last.lower() in student['last'].lower()]
        
        #Match Partial        
        if not match['students']:            
            match['students'] = [student for student in json_data['students'] if first.lower() in student['first'].lower() or first.lower() in student['last'].lower() or last.lower() in student['last'].lower() or last.lower() in student['first'].lower()]

        match['students'] = {unique['email']:unique for unique in match['students']}.values()
        return json.loads(json.dumps(match))

    #Pulls in the classes document
    def get_classes():
        classes = json_data['classes']
        return classes


