# Rest API in Flask
<img src="img/designk.jpeg" width="700" height="400" style="margin-left: 200px; margin-top: 50px"/>

In order to understand how to design REST API's in Flask, Let's work on a simple example. Let's not worry about authentication or having multiple user accounts in this example. Let's create a simple TODO app where you can keep track of TODO items. For simplicity we will not deal with database part for now. All data for this application will be in the memory. I have worked out a simple design for this app in a paper.

## Part 01
Let's start with something simple. Lets define tasks API as follows as a begining.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/tasks')
def tasks():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

## Part 02
In order to consume this service, we can use following client. Also, you can write your own client using language of your choice or curl.

```python
import requests

def main():
    res = requests.get('http://localhost:5000/tasks')
    print (res.text)

if __name__ == '__main__':
    main()
```

<img src="img/client1.png" width="700" height="50" style="margin-left: 200px; margin-top: 50px"/>

<img src="img/server1.png" width="700" height="70" style="margin-left: 200px; margin-top: 50px"/>

First go ahead an start server in one terminal, in another terminal use client to access the server. If server starts properly, you could see an output similer to above output.

Lets go ahead and implement function to create tasks. Task entity is defined as follows.

```
Task
{
    id: <int>,
    headline: <string>,
    status: <string>,
    priority: <int>,
    description: <string>,
}
```

```
POST /tasks
returns Task
```

First I have updated client to send JSON request to the service as follows.

```python
import requests
import json

def main():
    data = {'headline': 'task 01', 'description': 'Adding first task'}
    headers = {'Content-Type': 'application/json'}
    res = requests.post('http://localhost:5000/tasks', headers=headers, data=json.dumps(data))
    print (res.text)

if __name__ == '__main__':
    main()

```

In order to serve above request, I updated services as follows.

```python
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

```
As in the first step, run server in one terminal and send request from client in another terminal.

<img src="img/client2.png" width="800" height="250" style="margin-left: 200px; margin-top: 50px"/>

## Part 03
Keep in mind that we have all of these tasks/data in memory. Everytime server restarts we loose our data. We use this design just to get an exposure to REST api development. Now let's go ahead and add GET function implementation in tasks. 

```
GET /tasks
return [<Tasks>]
filters status, priority
```

It will return array of tasks. Also, we should be able to filter them based on task status and priority. I have updated client as follows

```python
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
```

From the services, we have only one line change to get the tasks in memory.
Only change we did, was in tasks function, therefore I will update only that.

```python
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    ...
    ...
    return jsonify(result=dict(status='success', data=list(config['tasks'].values())))

```
<img src="img/client3.png" width="800" height="450" style="margin-left: 200px; margin-top: 50px"/>
