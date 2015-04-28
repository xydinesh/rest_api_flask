# Rest API in Flask
<img src="img/designk.jpeg" width="700" height="400" style="margin-left: 200px; margin-top: 50px"/>

In order to understand how to design REST API's in Flask, Let's work on a simple example. Let's not worry about authentication or having multiple user accounts in this example. Let's create a simple TODO app where you can keep track of TODO items. For simplicity we will not deal with database part for now. All data for this application will be in the memory. I have worked out a simple design for this app in a paper.

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
* What is REST API
* Explain small example, simple blog example
* Using Flask to implement it