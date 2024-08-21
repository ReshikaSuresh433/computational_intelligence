import heapq

graph = {}
reverse_node_map = {}

def add_vertex(vertex):
    if vertex not in graph:
        graph[vertex] = []

def add_edge(vertex1, vertex2, cost):
    if vertex1 not in graph:
        add_vertex(vertex1)
    if vertex2 not in graph:
        add_vertex(vertex2)
    graph[vertex1].append((vertex2, cost))
    graph[vertex2].append((vertex1, cost))

def delete_edge(v1, v2):
    if v1 in graph and v2 in graph:
        graph[v1] = [edge for edge in graph[v1] if edge[0] != v2]
        graph[v2] = [edge for edge in graph[v2] if edge[0] != v1]
        print("Edge deleted")
    else:
        print("One or both nodes do not exist")

def delete_node(node):
    if node in graph:
        for neighbor, cost in graph[node]:
            graph[neighbor] = [edge for edge in graph[neighbor] if edge[0] != node]
        del graph[node]
        print(f"Node {node} and its edges have been deleted.")
    else:
        print(f"Node {node} not found in the graph.")

def bfs(start, end):
    if start not in graph or end not in graph:
        print(f"Node {start} or {end} not found in the graph.")
        return

    visited = set()
    queue = [(start, [start])]

    while queue:
        vertex, path = queue.pop(0)
        if vertex == end:
            print(f"Path from {start} to {end}: {' -> '.join(path)}")
            return

        for neighbor, cost in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                

    print(f"No path found from node {start} to node {end}")

def dfs(start, end, visited=None, path=None):
    if start not in graph or end not in graph:
        print(f"Node {start} or {end} not found in the graph.")
        return None

    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == end:
        return path

    for neighbor, cost in graph[start]:
        if neighbor not in visited:
            new_path = dfs(neighbor, end, visited, path)
            if new_path:
                return new_path

    if end not in path:
        print(f"Node {end} not reachable from {start}: {' -> '.join(path)}")
    return None

def ucs(start, goal):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        path = path + [current_node]
        if current_node == goal:
            return (cost, path)
        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))

    return None  # Explicitly return None if the goal is not found

def display():
    for node in graph:
        edges = ', '.join([f"({neighbor}, cost: {cost})" for neighbor, cost in graph[node]])
        print(f"{node}: {edges}")

def menu():
    global reverse_node_map
    while True:
        print("\nMenu:")
        print("1. Create Graph")
        print("2. Add edge")
        print("3. Delete node")
        print("4. Delete edge")
        print("5. Perform BFS")
        print("6. Perform DFS")
        print("7. Perform UCS")
        print("8. Display graph")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            graph.clear()
            reverse_node_map.clear()
            num_ver = int(input("Enter the number of vertices: "))
            num_edg = int(input("Enter the number of edges: "))
            for i in range(num_ver):
                vertex = input(f"Enter the vertex {i+1}: ")
                add_vertex(vertex)
            for i in range(num_edg):
                vertex1 = input(f"Enter vertex1 for edge {i+1}: ")
                vertex2 = input(f"Enter vertex2 for edge {i+1}: ")
                cost = int(input(f"Enter cost for edge {i+1}: "))
                add_edge(vertex1, vertex2, cost)
        elif choice == '2':
            u = input("Enter the first node: ")
            v = input("Enter the second node: ")
            cost = float(input("Enter the cost of the edge: "))
            add_edge(u, v, cost)
            print(f"Edge between {u} and {v} with cost {cost} added.")
        elif choice == '3':
            node = input("Enter the node to delete: ")
            delete_node(node)
        elif choice == '4':
            v1 = input("Enter the vertex1 of edge: ")
            v2 = input("Enter the vertex2 of edge: ")
            delete_edge(v1, v2)
        elif choice == '5':
            start = input("Enter the starting node for BFS: ")
            end = input("Enter the ending node for BFS: ")
            print(f"Breadth-First Search starting from vertex {start}:")
            bfs(start, end)
        elif choice == '6':
            start = input("Enter the starting node for DFS: ")
            end = input("Enter the ending node for DFS: ")
            result = dfs(start, end)
            if result:
                print(f"Path found from {start} to {end}: {' -> '.join(result)}")
            else:
                print(f"No path found between {start} and {end}")
        elif choice == '7':
            start = input("Enter the starting node for UCS: ")
            end = input("Enter the ending node for UCS: ")
            print(f"Uniform Cost Search starting from vertex {start}:")
            result = ucs(start, end)
            if result:
                cost, path = result
                print(f"Path found with cost {cost}: {' -> '.join(path)}")
            else:
                print("Goal not found")
        elif choice == '8':
            print("Graph:")
            display()
        elif choice == '9':
            break

menu()
