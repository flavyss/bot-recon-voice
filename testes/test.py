userinfo = open('data-user/user.json', 'w')
userinfo.write('''
    {
        "nome": "flavyson"
    }
''')
userinfo.close()

with open("data-user/user.json") as jsonFile:
    dados = json.load(jsonFile)
nick = dados['nome']


print(f'nome: {nick}')