class Node:
    def __init__(self, name, root):
        self.neighbours = {}
        self.name = name
        self.root = root

    def get_name(self):
        return self.name

    def add_neighbours(self, neighbour, cost):
        self.neighbours[neighbour] = cost

    def get_neighbours(self):
        return self.neighbours


def parser(nodes_arr):
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
            nodes_arr.append(Node(line[0], line[4]))
        elif count == 2:
            source_dest_cost = line.split(" : ")
            source_dest, cost = source_dest_cost[0], source_dest_cost[1]
            source_node, destination_node = source_dest.split(" - ")
            cost = cost.strip(";")
            for node in nodes:
                if node.name == source_node:
                    node.add_neighbours(destination_node, int(cost))

def get_root(nodes_arr):
    print("TLRD: Muss noch gemacht werden")

if __name__ == "__main__":
    nodes = []
    parser(nodes)

