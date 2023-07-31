import requests as rq

link = 'http://127.0.0.1:5000/vendas'

requisicao = rq.get(link)


print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()

print(dicionario['total_vendas'])
