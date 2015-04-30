from flask import (Flask, request, jsonify)
import json

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

	return jsonify(result=dict(status='success', data=list(config['tasks'].values())))

@app.route('/tasks/<int:id>', methods=['GET', 'POST'])
def task(id):
	task = config['tasks'].get(id, None)
	if task is None:
		return jsonify(result=dict(status='fail', data=None))

	if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
		headline = request.json.get('headline', None)
		description = request.json.get('description', None)
		status = request.json.get('status', None)
		priority = request.json.get('priority', None)

		if headline is not None:
			task['headline'] = headline
		if description is not None:
			task['description'] = description
		if status is not None:
			task['status']  = status
		if priority is not None:
			task['priority'] = priority

		config['tasks'][id] = task

		return jsonify(result=dict(status='success', data=task))
	return jsonify(result=dict(status='success', data=config['tasks'][id]))

if __name__ == '__main__':
    app.run(debug=True)
