from flask import Flask, jsonify, request

app = Flask(__name__)

from tasks import Tasks

# Get Data Routes
@app.route('/tasks', methods=['GET'])
def getTasks():
    return jsonify({'tasks':Tasks})


@app.route('/tasks/<int:id>', methods=['GET'])
def getTask(id):
    for task in Tasks:
        if task['id'] == id:
            return jsonify({'task': task})
    return jsonify({'message': 'Task not found'})

@app.route('/tasks', methods=['POST'])
def createTask():
    try:
        new_task = {
            'id': request.json['id'],
            'title': request.json['title'],
            'description': request.json['description'],
            'is_completed': request.json['is_completed']
        }
        Tasks.append(new_task)
        return jsonify({'task': new_task}), 201
    except Exception as e:
        return jsonify({'message': 'Invalid data'}), 400

@app.route('/tasks/<int:id>', methods=['PUT'])
def updateTask(id):
    for task in Tasks:
        if task['id'] == id:
            task['title'] = request.json['title']
            task['description'] = request.json['description']
            task['is_completed'] = request.json['is_completed']
            return jsonify({'task': task})
    return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def deleteTask(id):
    for task in Tasks:
        if task['id'] == id:
            Tasks.remove(task)
            return jsonify({'message': 'Task deleted'})
    return jsonify({'message': 'Task not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, port=4000)