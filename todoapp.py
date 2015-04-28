from flask import (Flask, request, jsonify)
app = Flask(__name__)

config = {}
config['tasks_id'] = 0
config['tasks'] = {}

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
	if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
		headline = request.json.get('headline', None)
		description = request.json.get('description', None)
		status = request.json.get('status', 'open')
		priority = request.json.get('priority', 3)
		if headline is None:
			return jsonify(result=dict(status='fail', description='Task headline not found'))
		config['tasks_id'] += 1
		config['tasks'][config['tasks_id']] = dict(id=config['tasks_id'], headline=headline, description=description, status=status, priority=priority)
		return jsonify(result=dict(status='success', data=config['tasks'][config['tasks_id']]))
	return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
