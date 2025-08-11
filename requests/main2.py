import requests

response = requests.get('http://172.25.253.124:5000/alunos')

print(response.status_code)

dados = {'nome': 'Pezin', 'email': 'pezinreidelas244@gmail.com', 'id': '7'}

response = requests.post('http://172.25.253.124:5000/alunos', json=dados)

print(response.status_code)
print(response.json())