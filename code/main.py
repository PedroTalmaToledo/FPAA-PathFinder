import heapq

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
                return (i, j)
    return None

def heuristic(a, b):
    # Distância de Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(pos, maze):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita
    result = []
    rows, cols = len(maze), len(maze[0])
    for d in directions:
        ni, nj = pos[0] + d[0], pos[1] + d[1]
        if 0 <= ni < rows and 0 <= nj < cols:
            if maze[ni][nj] != '1':
                result.append((ni, nj))
    return result

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def a_star(maze, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            return reconstruct_path(came_from, current)

        for neighbor in neighbors(current, maze):
            tentative_g_score = g_score[current] + 1  # custo sempre 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # Sem solução

def print_path_coordinates(path, start, end):
    coords = []
    for idx, p in enumerate(path):
        if p == start:
            coords.append(f"s{p}")
        elif p == end:
            coords.append(f"e{p}")
        else:
            coords.append(str(p))
    print("Menor caminho (em coordenadas):")
    print(coords)

def print_maze_with_path(maze, path):
    maze_cp = [row[:] for row in maze]
    for pos in path:
        i, j = pos
        if maze_cp[i][j] not in ['S', 'E']:
            maze_cp[i][j] = '*'
    print("\nLabirinto com o caminho destacado:")
    for row in maze_cp:
        print(' '.join(row))

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

    path = a_star(maze, start, end)
    if path is None:
        print("Sem solução")
    else:
        print_path_coordinates(path, start, end)
        print_maze_with_path(maze, path)

if __name__ == "__main__":
    main()
