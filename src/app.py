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

if __name__ == '__main__':
    app.run(debug=True, port=4000)