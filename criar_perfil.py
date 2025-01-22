
perfis = []

def criar_perfil(nome, email = None, *habilidades, **informacoes_adicionais):
    global perfis

    item = {
        'nome': nome,
        'email': email,
        'habilidades': habilidades,
        'informacoes_adicionais': informacoes_adicionais.items(),
    }

    perfis.append(item)
    return item


print(criar_perfil('José Beto'))
criar_perfil('Christian Oliveira', 'email@test.com')
criar_perfil('Edson Misael', 'email@test.com', {'habilidade': 'rápido'}, {'habilidade': 'inteligente'})

print("\n\n Perfis:")
print(perfis)