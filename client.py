import requests
import json

def main():
	data = {'headline': 'task 01', 'description': 'Adding first task'}
	headers = {'Content-Type': 'application/json'}
	res = requests.post('http://localhost:5000/tasks', headers=headers, data=json.dumps(data))
	print (res.text)
	res = requests.get('http://localhost:5000/tasks')
	print (res.text)

if __name__ == '__main__':
	main()
