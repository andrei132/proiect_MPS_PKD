from fileReader import FileReader

"""
    Calculates the f-measure for a value given by tree,
    saves the best result and tree and returns the result
    """
class FMeasure:
    def __init__(self, lutFile: FileReader):
        self.lutFile = lutFile
        self.best_result = -1
        self.best_tree = None

    def calculate_f_measure(self, tree_output: float, line: int, tree) -> float:
        idx = round(tree_output * 255)
        result = self.lutFile.get_element(line, idx)
        if result > self.best_result:
            self.best_result = result
            self.best_tree = tree
        return result

    def get_best_result(self):
        return self.best_result

    def get_best_tree(self):
        return self.best_tree