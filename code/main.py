def read_maze():
    print("Digite o labirinto linha por linha, separando os elementos por espaço.")
    print("Use 'S' para início, 'E' para fim, '0' para livre e '1' para obstáculo.")
    print("Exemplo de linha: S 0 1 0 0")
    print("Digite uma linha vazia para terminar.\n")

    maze = []
    while True:
        line = input()
        if not line.strip():
            break
        row = line.strip().split()
        maze.append(row)
    return maze


def find_point(maze, point):
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == point:
                return i, j
    return None


def main():
    maze = read_maze()
    if not maze:
        print("Labirinto vazio!")
        return

    start = find_point(maze, 'S')
    end = find_point(maze, 'E')

    if not start or not end:
        print("Erro: O labirinto deve conter um ponto inicial 'S' e um final 'E'.")
        return


if __name__ == "__main__":
    main()
