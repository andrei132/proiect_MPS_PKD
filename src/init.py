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

    # Best find in 15 sec
    best_f_measure = -1
    best_tree = None

    f_Measures = []
    t_end = time.time() + 15 # run 0.2 sec
    number_of_algorithm = len(csv_global_file.get_line(0))

    while time.time() < t_end:
        f_Measures = []
        tree = rTree.RandomTree.generate_random_tree()
        random_algorthm = rAlgorithm.random_numers_between(number_of_algorithm, rAlgorithm.random_choice(data=3, end=number_of_algorithm))
        i = 0
        for line in csv_global_file.get_result():
            f_Measure = fMeasure.FMeasure(csv_lut_file)
            new_tree = copy.deepcopy(tree)
            values = [float(line[i]) for i in random_algorthm]
            new_tree.add_data_in_tree(values)
            f_Measure.calculate_f_measure(new_tree.get_tree_result(), i, new_tree)
            i+=1
            f_Measures.append(f_Measure)

        # Check if is the best tree
        avg_f_measure = sum(x.best_result for x in f_Measures) / len(f_Measures)
        if (avg_f_measure > best_f_measure):
            best_f_measure = avg_f_measure
            best_tree = f_Measures[0].best_tree

    print(best_f_measure)
    best_tree.show()