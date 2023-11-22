import randomTree as rTree
import fileReader as fReader
import randomAlgorithm as rAlgorithm
import fMeasure
import sys
import time
import copy


if __name__ == "__main__":
    print(sys.argv[1], sys.argv[2])
    csv_lut_file = fReader.FileReader(sys.argv[1])
    csv_global_file = fReader.FileReader(sys.argv[2])

    csv_lut_file.csv_read()
    csv_global_file.csv_read()

    f_Measure  = fMeasure.FMeasure(csv_lut_file)
    
    t_end = time.time() + 0.2 # run 0.2 sec
    number_of_algorithm = len(csv_global_file.get_line(0))
    
    while time.time() < t_end:
        tree = rTree.RandomTree.generate_random_tree()
        random_algorthm = rAlgorithm.random_numers_between(number_of_algorithm, rAlgorithm.random_choice(data=3, end=number_of_algorithm))
        for line in [csv_global_file.get_line(0)]:
            new_tree = copy.deepcopy(tree)
            values = [float(line[i]) for i in random_algorthm]
            new_tree.add_data_in_tree(values)
            f_Measure.calculate_f_measure(new_tree.get_tree_result(), 0, new_tree)
    print(f_Measure.best_result)
    f_Measure.best_tree.show()