import csv
import sys

def lerArquivo(title):
    try:
        with open(f"{title}") as file:
            content = csv.reader(file, delimiter=';')
            data = list(content)
        return data
    except FileNotFoundError:
        return None

def criarGrafo(automato):
    grafo = {}
    for item in automato:
        origem, destino, peso = item[0], item[1], item[2]
        # Se o vértice de origem não está no grafo, adiciona ele
        if origem not in grafo:
            grafo[origem] = {}
        # Adiciona a aresta ao grafo
        grafo[origem][destino] = peso
    return grafo

def buscaEmProfundidade(grafo, origem, destino):
    # Pilha para o DFS
    pilha = [(origem, [origem])] # lista que contem uma tupla com a origem e uma lista dos caminhos (começa na origem)
    visitados = []
    while pilha:
        # Pega o automato atual e o caminho
        (vertice, caminho) = pilha.pop()
        if vertice not in visitados:
            visitados.append(vertice)
            # Para cada vizinho do automato atual no grafo
            for vizinho in grafo[vertice]:
                if grafo[vertice][vizinho] == '&':
                    if destino in vizinho:
                        return caminho + [vizinho]
                    else:
                        # adiciona à pilha o vizinho (proximo a ser percorrido) e atualização do caminho
                        pilha.append((vizinho, caminho + [vizinho]))
    return None

def mostrarGrafo(grafo):
    for vertice, arestas in grafo.items():
        for destino, peso in arestas.items():
            print(f"{vertice} -> {peso} -> {destino}")

if __name__ == '__main__':
    automatos = lerArquivo(sys.argv[1])
    grafo = criarGrafo(automatos)

    automatoInicial = sys.argv[2]
    automatoFinal = sys.argv[3]

    mostrarGrafo(grafo)
    
    if automatoFinal == automatoInicial:
        print(f"O automato inserido reconhece palavra vazia\nCaminho da palavra vazia: ['{automatoInicial}', '{automatoFinal}']")
        sys.exit()

    caminho = buscaEmProfundidade(grafo, automatoInicial, automatoFinal)

    if caminho is not None:
        print(f"O automato inserido reconhece palavra vazia\nCaminho da palavra vazia: {caminho}")
    else:
        print(f"O automato inserido reconhece gera palavra vazia")