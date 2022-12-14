from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from logic.person import Person


app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)

@app.route('/update', methods=['POST'])
def update():
    for person in model:
        if person.id_person == request.form['id_person']:
            person.first_name = request.form['first_name']
            person.last_name = request.form['last_name']
    persona = Person(id_person=request.form['id_person'], name=request.form['first_name'], last_name=request.form['last_name'])
    return render_template('person_detail.html', value=persona)


@app.route('/person_update/<string:id>', methods=['GET'])
def person_update(id):
    information = 0
    for person in model:
        if person.id_person == id:
            information = person

    return render_template('person_update.html', data=information)


@app.route('/person_delete/<string:id>')
def person_delete(id):
    for person in model:
        if person.id_person == id:
            model.remove(person)

    return redirect('/people')

if __name__ == '__main__':
    app.run(debug=True)
