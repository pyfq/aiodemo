# aiodemo

a todo demo based on aiohttp、aiomysql、sqlalchamy

\>>> import requests  
\>>> resp = requests.post('http://localhost:8080/todos', json={'content': 'fisrt todo'})  
\>>> resp.status_code  
200  
\>>> resp = requests.get('http://localhost:8080/todos')  
\>>> resp.json()  
[{u'content': u'fisrt todo', u'finished': u'no', u'id': 1}]  
\>>> resp = requests.patch('http://localhost:8080/todos/1', json={'finished': 'yes'})  
\>>> resp.status_code  
204  
\>>> resp = requests.get('http://localhost:8080/todos/1')  
\>>> resp.json()  
{u'content': u'fisrt todo', u'finished': u'yes', u'id': 1}  
\>>> resp = requests.delete('http://localhost:8080/todos/1')  
\>>> resp.status_code  
204  
\>>> resp = requests.get('http://localhost:8080/todos/1')  
\>>> resp.json()  
{u'error': u'Todo not found'}