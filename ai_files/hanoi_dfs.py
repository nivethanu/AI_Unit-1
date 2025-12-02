# hanoi_dfs.py
# DFS Recursive solution for Tower of Hanoi (3 disks, 3 pegs)

def hanoi_dfs(n, source, target, auxiliary, moves):
    # Base condition: no disk to move
    if n == 0:
        return
    
    # Step 1: Move n-1 disks from source -> auxiliary
    hanoi_dfs(n-1, source, auxiliary, target, moves)

    # Step 2: Move the largest disk from source -> target
    moves.append((source, target))

    # Step 3: Move n-1 disks from auxiliary -> target
    hanoi_dfs(n-1, auxiliary, target, source, moves)


if __name__ == "__main__":
    n = 3   # number of disks
    moves = []

    hanoi_dfs(n, "A", "C", "B", moves)

    print(f"Total moves: {len(moves)}")
    for i, (s, t) in enumerate(moves, 1):
        print(f"{i}: Move disk from {s} -> {t}")
