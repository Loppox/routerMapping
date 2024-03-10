class Node:
    def __init__(self, name, root):
        self.neighbours = {}
        self.name = name
        self.root = root
        self.root_cost = 0
        self.message_queue = []

    def receive_message(self, content: []):
        self.message_queue.append(content)

    def broadcast_message(self):
        costs = list(self.neighbours.values())
        i = 0
        message = [self.name, self.root, costs[i]]
        for neighbour in list(self.neighbours.keys()):
            neighbour.receive_message(message)
            i += 1

    def update_root(self, root: str, cost: int):
        self.root = root
        self.root_cost = cost

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node: Node):
        self.nodes.append(node)


def parser(graph: Graph):
    file = open("graph_input", "r")
    lines = file.readlines()
    count = 0
    for line in lines:
        line = line.strip()
        if line.__contains__("Node") or line.__contains__("Links"):
            count += 1
        elif line.__contains__("}"):
            break
        elif count == 1:
            graph.nodes.append(Node(line[0], int(line[4])))
        elif count == 2:
            source_dest_cost = line.split(" : ")
            source_dest, cost = source_dest_cost[0], source_dest_cost[1]
            source_node, destination_node = source_dest.split(" - ")
            cost = cost.strip(";")
            for node in graph.nodes:
                if node.name == source_node:
                    for dest_node in graph.nodes:
                        if dest_node.name == destination_node:
                            node.neighbours[dest_node] = int(cost)
    file.close()


def get_root(graph: Graph):
    for node in graph.nodes:
        if len(node.message_queue) == 0:
            node.broadcast_message()
        else:
            messages = node.message_queue
            for message in messages:
                print(message)
                if node.root > message[1]:
                    node.update_root(message[1], message[2])




if __name__ == "__main__":
    graph = Graph()
    nodes = []
    parser(graph)
    get_root(graph)

    for node in graph.nodes:
        print(node.root)