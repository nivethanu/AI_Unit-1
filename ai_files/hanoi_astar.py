# hanoi_astar.py
# A* search solution for Tower of Hanoi (3 disks)

import heapq

def is_goal(state, n):
    return state[2] == tuple(range(n, 0, -1))

def neighbors(state):
    """Generate all possible next states."""
    res = []
    for i in range(3):
        if not state[i]:
            continue
        disk = state[i][-1]
        for j in range(3):
            if i == j:
                continue
            if not state[j] or state[j][-1] > disk:
                new_state = list(map(list, state))
                new_state[i].pop()
                new_state[j].append(disk)
                res.append((tuple(map(tuple, new_state)), (i, j)))
    return res

def heuristic(state, n):
    """
    Simple admissible heuristic:
    Count how many disks are NOT on the target peg (peg C).
    """
    return len(state[0]) + len(state[1])

def astar(n):
    start = (tuple(range(n, 0, -1)), (), ())
    pq = []
    heapq.heappush(pq, (heuristic(start, n), 0, start, []))
    visited = {}

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if is_goal(state, n):
            return path

        if state in visited and visited[state] <= g:
            continue
        visited[state] = g

        for nxt, move in neighbors(state):
            new_g = g + 1
            h = heuristic(nxt, n)
            new_f = new_g + h
            heapq.heappush(pq, (new_f, new_g, nxt, path + [move]))

    return None


if __name__ == "__main__":
    n = 3
    path = astar(n)

    if path is None:
        print("No solution found.")
    else:
        print(f"Total moves: {len(path)}")
        peg_names = ['A', 'B', 'C']
        for i, (s, t) in enumerate(path, 1):
            print(f"{i}: Move top disk from {peg_names[s]} -> {peg_names[t]}")
