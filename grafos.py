import networkx as nx
import matplotlib.pyplot as plt

# Função para criar um grafo a partir de uma lista de arestas
def criar_grafo(arestas, direcionado=False):
    if direcionado:
        G = nx.DiGraph() # grafo dicerionado
    else:
        G = nx.Graph() # grafo não direcionado
    G.add_edges_from(arestas)
    return G

# Função para exibir o grafo
def exibir_grafo(grafo, direcionado=False):
    if direcionado:
        nx.draw(grafo, with_labels=True, arrows=True)
    else:
        nx.draw(grafo, with_labels=True)
    plt.title("Grafo " + ("direcionado" if direcionado else "não direcionado"))
    plt.show()

# Criação do grafo
if __name__ == "__main__":
    arestas = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (5, 4)]

    tipo_grafo = input("Digite 'd' para grafo direcionado ou 'n' para grafo não direcionado: ")
    if tipo_grafo.lower() == 'd':
        grafo = criar_grafo(arestas, direcionado=True)
    else:
        grafo = criar_grafo(arestas)

    exibir_grafo(grafo, direcionado=(tipo_grafo.lower() == 'd'))