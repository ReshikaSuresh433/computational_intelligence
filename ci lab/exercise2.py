from queue import PriorityQueue

# Global variables
graph = {}
heuristics = {}

def add_node(node):
    if node not in graph:
        graph[node] = {}
    else:
        print("Node already exists.")

def delete_node(node):
    if node in graph:
        del graph[node]
        for neighbors in graph.values():
            if node in neighbors:
                del neighbors[node]
        if node in heuristics:
            del heuristics[node]
    else:
        print("Node not found.")

def add_edge(from_node, to_node, cost):
    if from_node not in graph:
        add_node(from_node)
    if to_node not in graph:
        add_node(to_node)
    graph[from_node][to_node] = cost
    graph[to_node][from_node] = cost  # Undirected graph

def delete_edge(from_node, to_node):
    if from_node in graph and to_node in graph[from_node]:
        del graph[from_node][to_node]
        del graph[to_node][from_node]  # Assuming undirected graph
    else:
        print("Edge not found.")

def set_heuristic(node, heuristic):
    heuristics[node] = heuristic

def set_heuristics_for_all(new_heuristics):
    """Set heuristics for multiple nodes"""
    global heuristics
    heuristics = new_heuristics

def display():
    print("Graph:")
    for node, neighbors in graph.items():
        print(f"{node}:")
        for neighbor, cost in neighbors.items():
            print(f"  -> {neighbor} (cost: {cost})")
    print("Heuristics:")
    for node, heuristic in heuristics.items():
        print(f"{node}: {heuristic}")

def A_star(start, destination):
    visited = set()
    queue = PriorityQueue()
    queue.put((0 + heuristics.get(start, 0), 0, [start]))  # (estimated_cost, cost_from_start, path)

    while not queue.empty():
        estimated_cost, cost, path = queue.get()
        vertex = path[-1]

        if vertex == destination:
            print("Reached destination with cost =", cost, "path =", path)
            return

        if vertex not in visited:
            visited.add(vertex)
            for neighbor, neighbor_cost in graph[vertex].items():
                if neighbor not in visited:
                    new_cost = cost + neighbor_cost
                    estimated_total_cost = new_cost + heuristics.get(neighbor, 0)
                    new_path = path + [neighbor]
                    queue.put((estimated_total_cost, new_cost, new_path))

    print("Destination not reachable")

# Initialize graph with predefined edges
edges_to_add = [
    ('Arad', 'Zerind', 75),
    ('Arad', 'Sibiu', 140),
    ('Arad', 'Timisoara', 118),
    ('Zerind', 'Oradea', 71),
    ('Oradea', 'Sibiu', 151),
    ('Sibiu', 'Fagaras', 99),
    ('Sibiu', 'Rimnicu Vilcea', 80),
    ('Fagaras', 'Bucharest', 211),
    ('Rimnicu Vilcea', 'Pitesti', 97),
    ('Pitesti', 'Bucharest', 101),
    ('Timisoara', 'Lugoj', 111),
    ('Lugoj', 'Mehadia', 70),
    ('Mehadia', 'Drobeta', 75),
    ('Drobeta', 'Craiova', 120),
    ('Craiova', 'Pitesti', 138)
]

for edge in edges_to_add:
    from_node, to_node, cost = edge
    add_edge(from_node, to_node, cost)

initial_heuristics = {
    'Arad': 366,
    'Zerind': 374,
    'Sibiu': 253,
    'Timisoara': 329,
    'Oradea': 380,
    'Fagaras': 178,
    'Rimnicu Vilcea': 193,
    'Pitesti': 98,
    'Bucharest': 0,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160
}

set_heuristics_for_all(initial_heuristics)

while True:
    print("1. Add Node")
    print("2. Add Edge")
    print("3. Delete Node")
    print("4. Delete Edge")
    print("5. Display Graph")
    print("6. A* Search")
    print("7. Set Heuristic")
    print("8. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        node = input("Enter a node to add: ")
        add_node(node)
    elif choice == '2':
        from_node = input("Enter the from node of the edge: ")
        to_node = input("Enter the to node of the edge: ")
        cost = int(input("Enter the cost of the edge: "))
        add_edge(from_node, to_node, cost)
    elif choice == '3':
        node = input("Enter the node to delete: ")
        delete_node(node)
    elif choice == '4':
        from_node = input("Enter the from node of the edge: ")
        to_node = input("Enter the to node of the edge: ")
        delete_edge(from_node, to_node)
    elif choice == '5':
        display()
    elif choice == '6':
        start = input("Enter the start node: ")
        destination = input("Enter the destination node: ")
        A_star(start, destination)
    elif choice == '7':
        node = input("Enter the node to set heuristic: ")
        heuristic = int(input(f"Enter the heuristic cost for {node}: "))
        set_heuristic(node, heuristic)
    elif choice == '8':
        break
    else:
        print("Invalid choice. Please try again.")
