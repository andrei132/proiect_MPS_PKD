import fileReader
import randomAlgorithm
import functions
import inspect

class RandomTree:
    """
    Generate and/or operate with tree and/or tree nodes.
    """
    def __init__(self, content):
        self.content = content
        self.children = []

    def add_child(self, tree):
        self.children.append(tree)
        
    def get_children(self):
        return self.children
    
    def get_content(self):
        return self.content
    
    def exec_function(self, *data):
        if callable(self.content):
            return self.content(*data)
        raise TypeError("Not a function")
    
    def show(self, level=0):
        print("    " * level, self.content)
        for child in self.children:
            child.show(level + 1)

    
    @staticmethod
    def generate_random_tree(data_line):
        """
        Generate a randomized tree from leaves up to the root.
        """

        # get available tree functions (functions to process data from csv)
        node_functions = []
        for name in dir(functions):
            obj = getattr(functions, name)
            if inspect.isfunction(obj):
                node_functions.append(name)
                

        nodes = []
        
        values_count = randomAlgorithm.random_choice(1, len(data_line))
        # choose random amount of values to be leaf nodes
        choosen_values = randomAlgorithm.random_choice(data=data_line, number=values_count)

        tmp = []
        for value in choosen_values:
            tmp.append(RandomTree(value))
        
        nodes.append(tmp)

        # get a random number of levels which the result tree will be made of
        # (leaves and root count as levels)
        levels_count = randomAlgorithm.random_choice(3, 7)

        # for each level
        for i in range(1, levels_count - 1):
            tmp = []
            # get a random number of nodes on level
            nodes_on_level = randomAlgorithm.random_choice(3, 7)
            # for each new node
            for _ in range(nodes_on_level):
                # set a random function as content
                tmp_tree = RandomTree(randomAlgorithm.random_choice(node_functions))
                # get a random number of connections with lower-level nodes
                connections_with_lower_level_count = randomAlgorithm.random_choice(1, len(nodes[i-1]))
                selected_connections = randomAlgorithm.random_choice(data=nodes[i-1], number=connections_with_lower_level_count)
                # establish connections
                for connection in selected_connections:
                    tmp_tree.add_child(connection)
                tmp.append(tmp_tree)
            nodes.append(tmp)
        
        # set the root node
        output_node = RandomTree("OUTPUT")

        for node in nodes[-1]:
            output_node.add_child(node)

        return output_node
