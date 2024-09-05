class Node:
    def __init__(self, name: str, index: int):
        self.name = name
        self.colors = []
        self.neighbors = []
        self.index = index
        self.chosen_color = None

    def add_color(self, color):
        self.colors.append(color)

    def remove_color(self, color):
        if color in self.colors:
            self.colors.remove(color)

    def remove_first_color(self):
        if len(self.colors) == 0:
            return None

        return self.colors.pop(0)

    def add_neighbors(self, *neighbors):
        for neighbor in neighbors:
            self.neighbors.append(neighbor)

    def remove_neighbor(self, neighbor):
        self.neighbors.remove(neighbor)
