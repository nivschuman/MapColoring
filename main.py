from Node import Node
from MapColoring import MapPainter, ExcelMapPainter


def compare_nodes_func1(node1: Node, node2: Node):
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


def compare_nodes_func2(node1: Node, node2: Node):
    # least available colors
    if len(node1.colors) < len(node2.colors):
        return -1
    elif len(node1.colors) > len(node2.colors):
        return 1

    # in case of tie, minimum edges
    if len(node1.neighbors) > len(node2.neighbors):
        return 1
    elif len(node1.neighbors) < len(node2.neighbors):
        return -1

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

    return nodes, compare_nodes_func1


def generate_class_problem_nodes():
    colors = ["red", "green", "blue"]
    nodes = []

    node_b = Node("b", 0)
    node_b.colors = colors.copy()
    nodes.append(node_b)

    node_d = Node("d", 1)
    node_d.colors = colors.copy()
    nodes.append(node_d)

    node_e = Node("e", 2)
    node_e.colors = colors.copy()
    nodes.append(node_e)

    node_f = Node("f", 3)
    node_f.colors = colors.copy()
    nodes.append(node_f)

    node_g = Node("g", 4)
    node_g.colors = colors.copy()
    nodes.append(node_g)

    node_h = Node("h", 5)
    node_h.colors = colors.copy()
    nodes.append(node_h)

    node_i = Node("i", 6)
    node_i.colors = colors.copy()
    nodes.append(node_i)

    node_j = Node("j", 7)
    node_j.colors = colors.copy()
    nodes.append(node_j)

    node_k = Node("k", 8)
    node_k.colors = colors.copy()
    nodes.append(node_k)

    node_l = Node("l", 9)
    node_l.colors = colors.copy()
    nodes.append(node_l)

    node_m = Node("m", 10)
    node_m.colors = colors.copy()
    nodes.append(node_m)

    node_n = Node("n", 11)
    node_n.colors = colors.copy()
    nodes.append(node_n)

    node_o = Node("o", 12)
    node_o.colors = colors.copy()
    nodes.append(node_o)

    node_p = Node("p", 13)
    node_p.colors = colors.copy()
    nodes.append(node_p)

    node_b.add_neighbors(node_d, node_f, node_i)
    node_d.add_neighbors(node_b, node_g, node_e)
    node_e.add_neighbors(node_d, node_g)
    node_f.add_neighbors(node_b, node_h)
    node_g.add_neighbors(node_d, node_e, node_h, node_j)
    node_h.add_neighbors(node_f, node_l, node_k, node_g, node_i)
    node_i.add_neighbors(node_b, node_h, node_k, node_j)
    node_j.add_neighbors(node_i, node_g, node_k)
    node_k.add_neighbors(node_h, node_i, node_j, node_o, node_m)
    node_l.add_neighbors(node_h, node_m, node_o)
    node_m.add_neighbors(node_l, node_n, node_k)
    node_n.add_neighbors(node_m, node_p)
    node_o.add_neighbors(node_l, node_k)
    node_p.add_neighbors(node_i, node_n)

    return nodes, compare_nodes_func2


def main():
    nodes, compare_nodes_func = generate_class_problem_nodes()

    excel_map_painter = ExcelMapPainter(nodes, compare_nodes_func, "Solution.xlsx")
    solution_exists = excel_map_painter.paint_map()

    if not solution_exists:
        print("there is no solution!")
        return

    for node in nodes:
        print(f"{node.name} color is {node.chosen_color}")


if __name__ == '__main__':
    main()
