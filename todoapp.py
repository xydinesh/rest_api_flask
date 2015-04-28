from flask import Flask, request
app = Flask(__name__)

@app.route('/tasks')
def tasks():
	return 'Hello World!'

if __name__ == '__main__':
    app.run()
