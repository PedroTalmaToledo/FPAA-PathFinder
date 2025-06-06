# FPAA-PathFinder

## Integrantes:

- Ana Carolina de Carvalho Corrêa - ana.correa.1313117@sga.pucminas.br

- Júlia Evelyn de Oliveira Silva - jeosilva@sga.pucminas.br

- Matheus Nolasco Miranda Soares - matheus.nolasco@sga.pucminas.br

- Pedro Talma Toledo - pedrotoledo1717@gmail.com

# Descrição do Projeto

Este projeto implementa o ``algoritmo A*`` para encontrar o menor caminho entre dois pontos em um labirinto 2D, evitando obstáculos. O objetivo é ajudar um robô de resgate a se locomover do ponto inicial `S` até o ponto final `E`, considerando apenas movimentos válidos e o custo mínimo.

## Sobre o Problema

- O desafio consiste em navegar por um labirinto representado por uma matriz, onde:

    - `0` representa células livres

    - `1` representa obstáculos

    - `S` é o ponto inicial

    - `E` é o ponto final

O robô pode se mover para cima, baixo, esquerda ou direita, desde que não colida com obstáculos ou saia dos limites do labirinto. O custo de cada movimento é sempre `1`.

## Algoritmo A*

`A*` é um algoritmo de busca eficiente que combina:

- Custo real do caminho percorrido `(g(n))`: soma dos custos desde o início até o nó atual.
`Heurística (h(n))`: estimativa da distância até o destino. Neste projeto, usamos a distância de Manhattan:
`h(n) = |x_atual - x_final| + |y_atual - y_final|`

  - `A*` escolhe sempre o próximo nó com menor valor de `f(n) = g(n) + h(n)`, garantindo assim o menor caminho possível. 

## Como Executar

- Pré-requisitos

    - Python 3.x instalado

### Passos

- Clone este repositório ou copie o arquivo main.py.

- Execute o script:
    -   ````shell
        python main.py
        ````

- Digite o labirinto linha por linha, separando os elementos por espaço. Exemplo:

    ````shell
    S 0 1 0 0
    0 0 1 0 1
    1 0 1 0 0
    1 0 0 E 1
    ````

- Após digitar todas as linhas, pressione ``Enter`` em uma linha vazia para finalizar a entrada.

### O programa exibirá:

- O menor caminho encontrado (em coordenadas)

- O labirinto com o caminho destacado

### Exemplo de Entrada e Saída

- Entrada:

    ````shell
    S 0 1 0 0
    0 0 1 0 1
    1 0 1 0 0
    1 0 0 E 1
    ````
    

- Saída:

  ```shell
      Menor caminho (em coordenadas):
      ['s(0, 0)', '(1, 0)', '(1, 1)', '(2, 1)', '(3, 1)', '(3, 2)', 'e(3, 3)']

      Labirinto com o caminho destacado:
  
      S 0 1 0 0
      * * 1 0 1
      1 * 1 0 0
      1 * * E 1
  ```

- Se não houver solução possível, será exibido:

    ```shell
    Sem solução
    ```

## Funcionamento do Algoritmo
- O usuário insere o labirinto.

- O programa valida a existência dos pontos S e E.

- O algoritmo A* explora o labirinto, calculando para cada célula o custo total `(g(n) + h(n))`.

- Quando o ponto final é alcançado, o caminho é reconstruído e apresentado.

- Caso não exista caminho, o programa informa "Sem solução".

### Observações
- Apenas movimentos ortogonais (cima, baixo, esquerda, direita) são permitidos.