input = [['O', 'O', 'O', 'O'],
         ['D', 'O', 'D', 'O'],
         ['O', 'O', 'O', 'O'],
         ['X', 'D', 'D', 'O'], ]


def bfs(nodes):
    height = len(nodes)
    width = len(nodes[0])

    queue = []
    visited = set()
    queue.append((0, 0))

    pred = {}
    treasure_y, treasure_x = None, None

    # Explore
    while queue:
        y, x = queue.pop(0)
        visited.add((y, x))

        # Done
        if nodes[y][x] == 'X':
            treasure_y, treasure_x = y, x
            break

        # Look ahead
        moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for move_x, move_y in moves:
            if 0 <= move_x and move_x < width and 0 <= move_y and move_y < height:
                if nodes[move_y][move_x] != 'D' and (move_y, move_x) not in visited:
                    # this is a legal move, to somewhere new
                    queue.append((move_y, move_x))
                    pred[(move_y, move_x)] = y, x

    if not treasure_y:
        return 'No treasure'

    path = [(treasure_y, treasure_x)]

    previous = pred[(treasure_y, treasure_x)]
    while previous != (0, 0):
        path = [previous] + path
        previous = pred[previous]
    path = [(0, 0)] + path

    return path, len(path) - 1


path, length = bfs(input)
print(path, length)
