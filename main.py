import csv
import sys

import networkx as nx # pip install networkx
import matplotlib.pyplot as plt # pip install matplotlib

# https://networkx.org/documentation/stable/tutorial.html#drawing-graphs

def lerArquivo(title):
    try:
        with open(f"{title}.csv") as file:
            content = csv.reader(file, delimiter=';')
            data = list(content)
        return data
    except FileNotFoundError:
        return None

def criaGrafo(automato):
    grafo = {}
    for item in automato:
        origem, destino, peso = item[0], item[1], int(item[2])
        # Se o vértice de origem não está no grafo, adiciona ele
        if origem not in grafo:
            grafo[origem] = {}
        # Adiciona a aresta ao grafo
        grafo[origem][destino] = peso
    return grafo

def buscaEmProfundidade(grafo, origem):
    # Pilha para o DFS
    pilha = [(origem, [origem])] # lista que contem uma tupla com a origem e uma lista dos caminhos (começa na origem)
    while pilha:
        # Pega o automato atual e o proximo automato
        (vertice, caminho) = pilha.pop()
        # Para cada vizinho do automato atual no grafo
        for vizinho in grafo[vertice]:
            # Se a transição for -1
            if grafo[vertice][vizinho] == -1:
                # Se o vizinho é o automato final, retorna o caminho
                if 'qF' in vizinho:
                    return caminho + [vizinho]
                else:
                    # adiciona à pilha o vizinho (proximo a ser percorrido) e atualização do caminho
                    pilha.append((vizinho, caminho + [vizinho]))
    # Se não encontrar um caminho, retorna None
    return None

if __name__ == '__main__':
    automatos = lerArquivo(sys.argv[1])
    grafo = criaGrafo(automatos)

    automatoInicial = sys.argv[2]

    caminho = buscaEmProfundidade(grafo, automatoInicial)

    if caminho is not None:
        print(f"O automato inserido gera palavra vazia\nCaminho: {caminho}")
    else:
        print(f"O automato inserido não gera palavra vazia")

    DG = nx.DiGraph()
    DG.add_weighted_edges_from(automatos)

    plt.figure()
    pos = nx.shell_layout(DG) # planar_layout
    weight_labels = nx.get_edge_attributes(DG,'weight')
    nx.draw(DG,pos,with_labels = True,)
    nx.draw_networkx_edge_labels(DG,pos,edge_labels=weight_labels)
    plt.show()