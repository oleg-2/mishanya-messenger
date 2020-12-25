import requests

with open('server_route.txt', 'r', encoding='utf-8') as f:
    server_route = f.read()

zapros = server_route + 'msg.php?msg=deldel'
requests.get(zapros)
