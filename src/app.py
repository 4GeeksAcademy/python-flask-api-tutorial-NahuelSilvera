from flask import Flask, jsonify, request

app = Flask(__name__)


todos = [{"label": "Tarea 1", "done": False}]

@app.route('/todos', methods=['GET'])
def get_all_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body:", request_body)
    todos.append(request_body)
    return jsonify(todos), 200  


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        deleted_task = todos.pop(position)
        print(f"Tarea eliminada: {deleted_task}")
        return jsonify(todos), 200  
    except IndexError:
        return jsonify({"error": "Invalid position"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
