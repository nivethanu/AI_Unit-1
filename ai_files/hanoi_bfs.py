from collections import deque

def is_goal(state, n):
    return state[2] == tuple(range(n, 0, -1))

def neighbors(state):
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

def bfs(n):
    start = (tuple(range(n, 0, -1)), (), ())
    q = deque()
    q.append((start, []))
    visited = {start}

    while q:
        state, path = q.popleft()
        if is_goal(state, n):
            return path

        for nxt, move in neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, path + [move]))

    return None

if __name__ == "__main__":
    n = 3
    path = bfs(n)

    if path is None:
        print("No solution found.")
    else:
        print(f"Total moves: {len(path)}")
        peg_names = ['A', 'B', 'C']
        for i, (s, t) in enumerate(path, 1):
            print(f"{i}: Move top disk from {peg_names[s]} -> {peg_names[t]}")
