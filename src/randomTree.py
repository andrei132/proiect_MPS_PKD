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
        self._last_level_ = []

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

    def add_data_in_tree(self, data_line):
        if self._last_level_ == []:
            raise Exception("Non root node or tree was not generated random with generate_random_tree()")
        # values_count = randomAlgorithm.random_choice(1, len(data_line))
        
        for node in self._last_level_:
            # choosen_values = randomAlgorithm.random_choice(data=data_line, number=values_count)
            for value in data_line:
                node.add_child(RandomTree(value))
        return

    @staticmethod
    def generate_random_tree():
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
        
        values_count = randomAlgorithm.random_choice(3, len(node_functions))
        # choose random amount of values to be leaf nodes
        choosen_values = randomAlgorithm.random_choice(data=node_functions, number=values_count)

        last_level_tmp = []
        for value in choosen_values:
            last_level_tmp.append(RandomTree(value))
        nodes.append(last_level_tmp)

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
        output_node = RandomTree(randomAlgorithm.random_choice(node_functions))
        output_node._last_level_.extend(last_level_tmp)
        for node in nodes[-1]:
            output_node.add_child(node)

        return output_node

    @staticmethod
    def __execute_function__(name: str, data: list):
        """Find functioon by name and execute it with data

        Args:
            name (str): function name
            data (list): function argv

        Raises:
            Exception: Function not find

        Returns:
            float: return function's return
        """
        if name == "min_leafs":
            return functions.min_leafs(data)
        elif name == "max_leafs":
            return functions.max_leafs(data)
        elif name == "arithmetic_average":
            return functions.arithmetic_average(data)
        elif name == "geometric_average":
            return functions.geometric_average(data)
        elif name == "calculate_median":
            return functions.calculate_median(data)
        elif name == "log_limit":
            return functions.log_limit(data)
        elif name == "sin_limit":
            return functions.sin_limit(data)
        else:
            raise Exception("Function not find [" + name + "]")

    def get_tree_result(self) -> float:
        """
        Get tree result after all operation

        Raises:
            Exception: If tree has no leaf with floats

        Returns:
            float: Calculated value
        """
        if isinstance(self.content, float):
            return self.content

        values = []
        node:RandomTree
        for node in self.children:
            values.append(node.get_tree_result())
        if values == []:
            raise Exception("Bad Tree")
        return RandomTree.__execute_function__(self.content, values)