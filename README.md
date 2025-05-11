# FPAA-PathFinder

## Integrantes:

- Ana Carolina de Carvalho Corrêa - ana.correa.1313117@sga.pucminas.br

- Júlia Evelyn de Oliveira Silva - jeosilva@sga.pucminas.br

- Matheus Nolasco Miranda Soares- matheus.nolasco@sga.pucminas.br

- Pedro Talma Toledo - pedrotoledo1717@gmail.com

# Descrição do Projeto

Este projeto implementa o algoritmo A* para encontrar o menor caminho entre dois pontos em um labirinto 2D, evitando obstáculos. O objetivo é ajudar um robô de resgate a se locomover do ponto inicial `S` até o ponto final `E`, considerando apenas movimentos válidos e o custo mínimo.

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

`A*` escolhe sempre o próximo nó com menor valor de `f(n) = g(n) + h(n)`, garantindo assim o menor caminho possível.
