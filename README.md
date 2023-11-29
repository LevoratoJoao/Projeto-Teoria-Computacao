# Projeto-Teoria-Computacao

Este projeto é um software que determina se um dado automato gera ou não palavra vazia.

## Como usar

Para rodar o programa é necessário ter as seguintes bibliotecas instaladas:

- [Networkx](https://networkx.org/documentation/stable/index.html)

```bash
pip install networkx
```

- [Matplotlib](https://matplotlib.org/stable/)

```bash
pip install matplotlib
```

Apos instalar as bibliotecas, basta rodar o arquivo main.py, passar um arquivo .csv como argumento e o automato inicial.

```bash
python main.py <entrada.csv> <estado_inicial>
```

## Como funciona

O programa recebe um arquivo .csv com as informações do automato, estado atual, proximo estado e transição (transição vazia é representado com -1). Os arquivos de entrada seguem uma estrutura padrão se parados por ;, a primeira coluna é o estado atual, a segunda coluna é o proximo estado e a terceira coluna é a transição.

A partir dessas informações é criado um grafo usando dicionarios (chave: valor) onde cada vertice (chave) é um estado e o valor é também um dicionario com seus vertices adjacentes sendo as chaves (proximos estados) e pesos os valores (transições).

Apos a criação do grafo, é feita uma busca em profundidade modificada para verificar se o estado inicial consegue chegar a um estado final passando apenas por transições vazias.

Para isso criamos uma pilha (representada como uma lista em python) de tuplas que contem dois elementos, o primeiro é o estado atual (começa na origem) e o segundo é uma lista para o caminho percorrido.

Fazemos a execução da função enquanto a pilha tiver valores, dentro do while pegamos o vertice atual e o caminho e removemos elemento da pilha usando a função pop (função que remove e retorna o elemento removido, no caso como nossa pilha é uma lista de tuplas o valor retornado é uma tupla).

Após isso fazemos um for para percorrer os vertices adjacentes ao vertice atual, se a transição do atual para o vizinho for igual a -1 (transição vazia) verificamos se o vizinho é um estado final, se for atualizamos o caminho e retornamos ele, caso contrario, adicionamos o vizinho e a atualização do caminho à pilha e percorremos de novo. Caso a transição não seja -1 nós continuamos percorrendo os vizinhos, se nenhum deles tiver transição vazia nenhum valor novo é adicionado a pilha e o while termina.

Se o retorno da função for ```None``` o automato não gera palavra vazia, caso contrario ele gera e mostra o caminho percorrido.

No final do código é criado um grafo com o networkx e plotado com o matplotlib para uma visualização mais clara do automato.

## TODO

* Apresentar exemplos do funcionamento do programa com entrada e saída.
