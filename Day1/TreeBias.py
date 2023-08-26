def calculate_bias_and_depth(adj_list, node, parent, depth):
    total_bias = depth
    for neighbor in adj_list[node]:
        if neighbor != parent:
            total_bias += calculate_bias_and_depth(adj_list, neighbor, node, depth + 1)
    return total_bias

def main():
    n = int(input())  # Number of nodes
    adj_list = [[] for _ in range(n + 1)]  # Adjacency list representation of the tree

    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    bias = calculate_bias_and_depth(adj_list, 1, 0, 0)  # Start DFS from the root (node 1)

    print(bias)

if __name__ == "__main__":
    main()
