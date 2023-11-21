import functions

class RandomTree:
    def __init__(self, function):
        self.function = function
        self.children = []

    def add_child(self, function):
        tree_to_add = RandomTree(function)
        self.children.append(tree_to_add)
        return tree_to_add
        

    def get_children(self):
        return self.children
    
    def get_function(self):
        return self.function
    
    def exec_function(self, *data):
        return self.function(*data)
