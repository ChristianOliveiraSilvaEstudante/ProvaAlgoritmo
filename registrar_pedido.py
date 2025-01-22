
pedidos = []

def registrar_pedido(nome_cliente, endereco = None, *itens, **detalhes_adicionais):
    global pedidos

    item = {
        'cliente': nome_cliente,
        'endereco': endereco,
        'itens': itens,
        'detalhes_adicionais': detalhes_adicionais.items(),
    }

    pedidos.append(item)
    return item

print(registrar_pedido('José Beto'))
registrar_pedido('Christian Oliveira', 'Rua teste')
registrar_pedido('Edson Misael', 'Rua teste 2', {'item': 'batata', 'quantidade': 15}, {'item': 'hamburguer', 'quantidade': 1}, {'item': 'refrigerante', 'quantidade': 1})

print("\n\n Pedidos:")
print(pedidos)