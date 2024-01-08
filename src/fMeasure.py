from fileReader import FileReader

"""
    Calculates the f-measure for a value given by tree,
    saves the best result and tree and returns the result
    """
class FMeasure:
    def __init__(self, lutFile: FileReader = None):
        self.lutFile = lutFile
        self.best_result = -1
        self.best_tree = None
        self.tp = 0
        self.fp = 0
        self.fn = 0
        self.tn = 0

    def calculate_f_measure(self, tree_output: float, line: int, tree) -> float:
        idx = min(round(tree_output * 255), 255)
        result = self.lutFile.get_element(line, idx)

        if result > self.best_result:
            self.best_result = result
            self.best_tree = tree
        return result

    def get_best_result(self):
        return self.best_result

    def get_best_tree(self):
        return self.best_tree

    def calculate_f_measure_for_local(self):
        print(self.tp, self.tn, self.fp, self.fn)
        return self.tp / (self.tp + 0.5 * (self.fp + self.fn)) * 100

    def recalculate_tp_fp_fn_tn_for_local(self, local_file_csv: FileReader, line_index: int, threshold: float):
        pxl_value = local_file_csv.get_element(line_index, 0)
        pxl_class = local_file_csv.get_element(line_index, 1)

        calc_pxl_class = 1
        if threshold > pxl_value:
            calc_pxl_class = 0

        if calc_pxl_class == pxl_class and calc_pxl_class == 1:
            self.tp += 1

        if calc_pxl_class == pxl_class and calc_pxl_class == 0:
            self.tn += 1

        if calc_pxl_class != pxl_class and calc_pxl_class == 1:
            self.fp += 1

        if calc_pxl_class != pxl_class and calc_pxl_class == 0:
            self.fn += 1
