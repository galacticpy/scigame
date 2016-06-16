import sys
import pull_json

from flask import Flask, request, render_template

search = pull_json.search_students
classes = pull_json.get_classes()

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        query = request.form['search-students']
        count = 0
        students = search(request.form['search-students'])
        #Check if empty search results
        if not students['students']:
            noresults = True 
        else:
            noresults = False
            #Replaces studentClasses id with class name 
            for student in students['students']:
                count+=1
                for sclass in student['studentClasses']:
                    sclass['id'] = classes[str(sclass['id'])]
        return render_template('results.html', students=students, noresults=noresults,query=query,count=count)
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
