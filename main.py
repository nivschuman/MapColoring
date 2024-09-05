from Node import Node
from functools import cmp_to_key


def compare_nodes_func(node1: Node, node2: Node):
    # minimum remaining edges
    if len(node1.neighbors) > len(node2.neighbors):
        return 1
    elif len(node1.neighbors) < len(node2.neighbors):
        return -1

    # in case of tie, most remaining colors
    if len(node1.colors) > len(node2.neighbors):
        return -1
    elif len(node1.colors) < len(node2.neighbors):
        return 1

    # in case of tie, compare by index in list (left most node)
    return node1.index - node2.index


# function to select node based on given comparison function
def select_node(nodes, compare_nodes):
    sorted_nodes = sorted(nodes, key=cmp_to_key(compare_nodes))

    return None if len(sorted_nodes) == 0 else sorted_nodes[0]


# paint map, each node will return with chosen_color property set (if solution exists)
def paint_map(nodes, compare_nodes):
    selected_node = select_node(nodes, compare_nodes)

    # all nodes colored
    if selected_node is None:
        return True

    # get all neighboring nodes to selected node
    neighboring_nodes = list(filter(lambda node: selected_node in node.neighbors, nodes))

    painted_map = False

    for color in selected_node.colors:
        # remove selected node from nodes list
        nodes.remove(selected_node)

        # remove selected node from neighbors and the chosen color
        neighbor_has_no_colors = False

        for neighbor in neighboring_nodes:
            neighbor.remove_neighbor(selected_node)
            neighbor.remove_color(color)

            if len(neighbor.colors) == 0:
                neighbor_has_no_colors = True

        # neighbor was left without color to choose
        if neighbor_has_no_colors:
            # return selected node to nodes list
            nodes.append(selected_node)

            # return selected node and color to neighbors
            for neighbor in neighboring_nodes:
                neighbor.add_neighbors(selected_node)
                neighbor.add_color(color)

            # try next color
            continue

        # select color for selected node
        selected_node.chosen_color = color

        # paint map recursively
        painted_map = paint_map(nodes, compare_nodes)

        # return selected node to nodes list
        nodes.append(selected_node)

        # return selected node and color to neighbors
        for neighbor in neighboring_nodes:
            neighbor.add_neighbors(selected_node)
            neighbor.add_color(color)

        # if map was painted, return found solution
        if painted_map:
            return True

    # node failed to paint map with all available colors
    return False


def main():
    colors = ["red", "green", "blue"]
    nodes_dict = dict()
    nodes = []

    # initialize nodes_dict and nodes list
    for i in range(65, 81):
        node = Node(chr(i), i)

        for color in colors:
            node.add_color(color)

        nodes_dict[chr(i)] = node
        nodes.append(node)

    # initialize neighbors
    nodes_dict["A"].add_neighbors(nodes_dict["B"], nodes_dict["C"], nodes_dict["D"])
    nodes_dict["B"].add_neighbors(nodes_dict["A"], nodes_dict["C"], nodes_dict["E"])
    nodes_dict["C"].add_neighbors(nodes_dict["A"], nodes_dict["B"], nodes_dict["F"])
    nodes_dict["D"].add_neighbors(nodes_dict["A"], nodes_dict["L"], nodes_dict["G"])
    nodes_dict["E"].add_neighbors(nodes_dict["L"], nodes_dict["B"], nodes_dict["G"])
    nodes_dict["F"].add_neighbors(nodes_dict["C"], nodes_dict["M"], nodes_dict["G"], nodes_dict["O"])
    nodes_dict["G"].add_neighbors(nodes_dict["D"], nodes_dict["E"], nodes_dict["F"], nodes_dict["J"], nodes_dict["I"])
    nodes_dict["H"].add_neighbors(nodes_dict["O"])
    nodes_dict["I"].add_neighbors(nodes_dict["J"], nodes_dict["G"], nodes_dict["N"], nodes_dict["K"])
    nodes_dict["J"].add_neighbors(nodes_dict["G"], nodes_dict["I"])
    nodes_dict["K"].add_neighbors(nodes_dict["N"], nodes_dict["P"], nodes_dict["I"])
    nodes_dict["L"].add_neighbors(nodes_dict["D"], nodes_dict["E"], nodes_dict["M"])
    nodes_dict["M"].add_neighbors(nodes_dict["L"], nodes_dict["F"])
    nodes_dict["N"].add_neighbors(nodes_dict["P"], nodes_dict["I"], nodes_dict["K"])
    nodes_dict["O"].add_neighbors(nodes_dict["F"], nodes_dict["P"], nodes_dict["H"])
    nodes_dict["P"].add_neighbors(nodes_dict["N"], nodes_dict["K"], nodes_dict["O"])

    solution_exists = paint_map(nodes, compare_nodes_func)

    if not solution_exists:
        print("there is no solution!")
        return

    for node in nodes:
        print(f"{node.name} color is {node.chosen_color}")


if __name__ == '__main__':
    main()
