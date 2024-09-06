from functools import cmp_to_key


class Node:
    def __init__(self, name: str, index: int):
        self.name = name
        self.colors = []
        self.neighbors = []
        self.index = index
        self.chosen_color = None

    def add_color(self, color):
        if color not in self.colors:
            self.colors.append(color)

    def remove_color(self, color):
        if color not in self.colors:
            return False

        self.colors.remove(color)
        return True

    def add_neighbors(self, *neighbors):
        for neighbor in neighbors:
            self.neighbors.append(neighbor)

    def remove_neighbor(self, neighbor):
        self.neighbors.remove(neighbor)

    def sort_colors(self):
        self.colors = sorted(self.colors, key=cmp_to_key(self.compare_colors))

    @staticmethod
    def compare_colors(color1, color2):
        colors_list = ["red", "green", "blue"]

        # order does not matter
        if color1 not in colors_list or color2 not in colors_list:
            return 1

        return colors_list.index(color1) - colors_list.index(color2)