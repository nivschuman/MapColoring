from Node import Node
from MapColoring import MapPainter, ExcelMapPainter


def compare_nodes_func(node1: Node, node2: Node):
    # minimum remaining edges
    if len(node1.neighbors) > len(node2.neighbors):
        return 1
    elif len(node1.neighbors) < len(node2.neighbors):
        return -1

    # in case of tie, most remaining colors
    if len(node1.colors) > len(node2.colors):
        return -1
    elif len(node1.colors) < len(node2.colors):
        return 1

    # in case of tie, compare by index in list (left most node)
    return node1.index - node2.index


def generate_homework3_nodes():
    colors = ["red", "green", "blue"]
    nodes_dict = dict()
    nodes = []

    # initialize nodes_dict and nodes list
    index = 0
    for i in range(65, 81):
        node = Node(chr(i), index)

        for color in colors:
            node.add_color(color)

        nodes_dict[chr(i)] = node
        nodes.append(node)

        index += 1

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

    return nodes


def main():
    nodes = generate_homework3_nodes()

    excel_map_painter = ExcelMapPainter(nodes, compare_nodes_func, "HW3.xlsx")
    solution_exists = excel_map_painter.paint_map()

    if not solution_exists:
        print("there is no solution!")
        return

    for node in nodes:
        print(f"{node.name} color is {node.chosen_color}")


if __name__ == '__main__':
    main()
