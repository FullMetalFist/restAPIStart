#!flask/bin/python
from flask import Flask, jsonify, abort

app = Flask(__name__)

tasks = [
    {
        'id' : 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Bread, Fruit',
        'done': False
    },
    {
        'id' : 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    },
    {
        'id' : 3,
        'title': u'Travel',
        'description': u'research places you want to visit',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
    
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})