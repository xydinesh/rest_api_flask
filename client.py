import requests
import json

def main():
	headers = {'Content-Type': 'application/json'}
	data = {'headline': 'task 01', 'description': 'Updated task description for first test'}
	res = requests.post('http://localhost:5000/tasks/1', headers=headers, data=json.dumps(data))
	print (res.text)

if __name__ == '__main__':
	main()
