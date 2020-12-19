parent = [-1, 0, 0, 2, 2]

# ↑↑ to wystarcza...

# zadanie: stworzyć "lisę list", children, gdzie children[2] to lista dzieci elementu 2


def get_children(p):
    lista = []
    for i in range(len(p)):
        children = []
        for j in range(len(p)):
            if p[j] == i:
                children.append(j)
        lista.append(children)
    return lista


print(get_children(parent))