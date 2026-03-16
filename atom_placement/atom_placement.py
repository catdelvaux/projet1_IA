"""NAMES OF THE AUTHOR(S): Alice Burlats <alice.burlats@uclouvain.be>"""

from atom_placement_state import AtomPlacementState


class AtomPlacement:

    # An init state building is provided here but you can change it at will
    def init_state(self) -> AtomPlacementState:
        sites = []
        for atom_type, quantity in enumerate(self.n_types):
            for i in range(quantity):
                sites.append(atom_type)

        return AtomPlacementState(sites)

    # Returns the neighbor states of the given state as a list of AtomPlacementState
    def neighbors(self, state: AtomPlacementState) -> list[AtomPlacementState]:
        # TODO
        result=[]

        for u in range(self.n_sites):
            for v in range(u+1, self.n_sites):
                if state.sites_assignment[u] != state.sites_assignment[v]:
                    new_assignment = state.sites_assignment[:]
                    new_assignment[u], new_assignment[v] = new_assignment[v], new_assignment[u]
                    result.append(AtomPlacementState(new_assignment))

        return result

    # Returns the objective value of the given state
    def value(self, state: AtomPlacementState) -> int:
        # TODO
        total=0

        for edge in self.edges:
            type_u = state.sites_assignment[edge[0]]
            type_v = state.sites_assignment[edge[1]]
            total+=self.energy_matrix[type_u][type_v]

        return total

    def __init__(self, filename: str):
        file = open(filename)
        line = file.readline()
        self.n_sites = int(line.split(' ')[0])
        self.k = int(line.split(' ')[1])
        self.n_edges = int(line.split(' ')[2])
        self.edges = []
        file.readline()

        self.n_types = [int(val) for val in file.readline().split(' ')]
        if sum(self.n_types) != self.n_sites:
            print('Invalid instance, wrong number of sites')
        file.readline()

        self.energy_matrix = []
        for i in range(self.k):
            self.energy_matrix.append([int(val) for val in file.readline().split(' ')])
        file.readline()

        for i in range(self.n_edges):
            self.edges.append([int(val) for val in file.readline().split(' ')])



