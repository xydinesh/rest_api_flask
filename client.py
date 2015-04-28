import requests

def main():
	res = requests.get('http://localhost:5000/tasks')
	print (res.text)

if __name__ == '__main__':
	main()
