from collections import deque

def bfs_graph(start_node, graph):
    """
    Perform BFS on a graph.

    Parameters:
    - start_node: The starting node for BFS.
    - graph: The graph represented as an adjacency list (dictionary).

    Returns:
    - A list of nodes in the order they were visited.
    """
    visited = set()      # Set to keep track of visited nodes
    queue = deque([start_node])  # Initialize the queue with the start node
    order = []           # List to keep track of the order of visit

    while queue:
        node = queue.popleft()  # Dequeue a node from the front of the queue
        if node not in visited:
            visited.add(node)   # Mark the node as visited
            order.append(node)  # Record the node visit
            # Add all unvisited neighbors to the queue
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return order
print("Ahmed Shaikh 323");

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
bfs_order = bfs_graph(start_node, graph)
print("BFS Order:", bfs_order)
