# aiodemo

#### a todo demo based on aiohttp、aiomysql、sqlalchamy

#### Run:  
1. init database structure by <font color=#0099ff>todo.sql</font>
2. update db config to yours in <font color=#0099ff>config.py</font>
3. ```pip install -r requirements.txt```
4. ```python server.py```

#### Example:  
``` python
>>> import requests  
>>> resp = requests.post('http://localhost:8080/todos', json={'content': 'fisrt todo'})  
>>> resp.status_code  
200  
>>> resp = requests.get('http://localhost:8080/todos')  
>>> resp.json()  
[{u'content': u'fisrt todo', u'finished': u'no', u'id': 1}]  
>>> resp = requests.patch('http://localhost:8080/todos/1', json={'finished': 'yes'})  
>>> resp.status_code  
204  
>>> resp = requests.get('http://localhost:8080/todos/1')  
>>> resp.json()  
{u'content': u'fisrt todo', u'finished': u'yes', u'id': 1}  
>>> resp = requests.delete('http://localhost:8080/todos/1')  
>>> resp.status_code  
204  
>>> resp = requests.get('http://localhost:8080/todos/1')  
>>> resp.json()  
{u'error': u'Todo not found'}  
```