from collections import deque


class MapColoringCSP:
    """CSP for map coloring."""

    def __init__(self):
        """Initialize the MapColoringCSP."""
        self.variables = []
        self.domains = {}
        self.edges = []

    @staticmethod
    def _is_consistent(value, domain):
        for other_value in domain:
            if value != other_value:
                return True
        return False

    def _neighbors(self, x):
        neighbors = []
        for (x_i, x_j) in self.edges:
            if x_i == x:
                neighbors.append(x_j)
            if x_j == x:
                neighbors.append(x_i)

        return list(set(neighbors))

    def add_var(self, variable, domain):
        """
        Add a variable with its domain.
        :param str variable: variable name
        :param list[str] domain: list of color values
        """
        self.variables.append(variable)
        self.domains[variable] = domain

    def add_edge(self, x_i, x_j):
        """
        Add an edge on the map between x_i and x_j.
        :param str x_i: variable 1
        :param str x_j: variable 2
        """
        self.edges.append((x_i, x_j))
        self.edges.append((x_j, x_i))

    def ac3(self):
        """
        Perform the AC-3 algorithm to compute arc consistency.

        :return: True, if the variable assignment is consistent with the constraints, False otherwise.
        """
        queue = deque(self.edges)
        print("Starting AC-3 algorithm to check for arc consistency... \n")

        while queue:
            x_i, x_j = queue.popleft()

            print(f"QUEUE: {queue}")
            print(f"Checking arc ({x_i}, {x_j}):")
            if self._revise(x_i, x_j):
                if not self.domains[x_i]:
                    print("    Inconsistency found!\n")
                    return False
                for x_k in self._neighbors(x_i):
                    if x_k != x_j:
                        print(f"    Added ({x_k}, {x_i}) to queue.")
                        queue.append((x_k, x_i))
                print("\n")
        return True

    def _revise(self, x_i, x_j):
        """
        Revise the domain of x_i in relation to x_j.
        :param x_i: variable 1
        :param x_j: variable 2
        :return: True, if the domain of x_i was revised, False otherwise
        """
        revised = False
        old_domain = [color for color in self.domains[x_i]]

        for color in self.domains[x_i]:
            if not self._is_consistent(color, self.domains[x_j]):
                self.domains[x_i].remove(color)
                revised = True

        if revised:
            print(f"    {x_i}: {old_domain} <-> {x_j}: {self.domains[x_j]}")
            print(f"    Revised {x_i} to {self.domains[x_i]}")
        else:
            print("    No revision done.\n")

        return revised
