from os import listdir
from os.path import isfile, join
from multiprocessing import Process, current_process

import randomTree as rTree
import fileReader as fReader
import randomAlgorithm as rAlgorithm
import fMeasure
import time
import copy
import logging
import argparse
import concurrent.futures

def configure_logging():
    logging.basicConfig(filename='../logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def global_bin(lut_file_path, global_file_path):
    csv_lut_file = fReader.FileReader(lut_file_path)
    csv_global_file = fReader.FileReader(global_file_path)

    csv_lut_file.csv_read()
    csv_global_file.csv_read()

    # Best find in 15 sec
    best_f_measure = -1
    best_tree = None

    f_Measures = []
    t_end = time.time() + 3600
    number_of_algorithm = len(csv_global_file.get_line(0))
    logging.info(f'Numarul total de algoritmi : [{str(number_of_algorithm)}]')
    nr_of_trees = 0
    while time.time() < t_end:
        f_Measures = []
        logging.info(f'Se creeaza arborele cu numarul : [{str(nr_of_trees)}]')
        nr_of_trees += 1
        tree = rTree.RandomTree.generate_random_tree()
        random_algorthm = rAlgorithm.random_numers_between(number_of_algorithm, rAlgorithm.random_choice(data=3, end=7))
        logging.info(f'Numarul de algoritmi care v-a fi pe ultimul nivel al arborelui : [{str(len(random_algorthm))}]')
        i = 0
        new_tree = tree
        for line in csv_global_file.get_result():
            f_Measure = fMeasure.FMeasure(csv_lut_file)
            values = [float(line[i]) for i in random_algorthm]
            new_tree.add_data_in_tree(values)
            f_Measure.calculate_f_measure(new_tree.get_tree_result(), i, new_tree)
            i += 1
            f_Measures.append(f_Measure)
            new_tree.remove_last_level()

        # Check if is the best tree
        avg_f_measure = sum(x.best_result for x in f_Measures) / len(f_Measures)
        print(avg_f_measure)
        if avg_f_measure > best_f_measure:
            best_f_measure = avg_f_measure
            best_tree = f_Measures[0].best_tree
            best_tree.serialize(name=current_process().name)

    best_tree.score = best_f_measure
    print(best_f_measure)
    # best_tree.show()
    best_tree.serialize(name=current_process().name)
    # print(rTree.RandomTree.deserialize_all())

def global_bin_use_saved(lut_file_path, global_file_path, tree_to_use):
    csv_lut_file = fReader.FileReader(lut_file_path)
    csv_global_file = fReader.FileReader(global_file_path)

    csv_lut_file.csv_read()
    csv_global_file.csv_read()
    
    number_of_algorithm = len(csv_global_file.get_line(0))
    f_Measures = []
    tree = tree_to_use
    random_algorthm = rAlgorithm.random_numers_between(number_of_algorithm, rAlgorithm.random_choice(data=3, end=7))
    logging.info(f'Numarul de algoritmi care v-a fi pe ultimul nivel al arborelui : [{str(len(random_algorthm))}]')
    i = 0
    new_tree = tree
    for line in csv_global_file.get_result():
        f_Measure = fMeasure.FMeasure(csv_lut_file)
        values = [float(line[i]) for i in random_algorthm]
        new_tree.add_data_in_tree(values)
        f_Measure.calculate_f_measure(new_tree.get_tree_result(), i, new_tree)
        i += 1
        f_Measures.append(f_Measure)
        new_tree.remove_last_level()

        # Check if is the best tree
    avg_f_measure = sum(x.best_result for x in f_Measures) / len(f_Measures)
    best_f_measure = avg_f_measure
    best_tree = f_Measures[0].best_tree

    best_tree.score = best_f_measure
    print(best_f_measure)
    # best_tree.show()
    # best_tree.serialize(name=current_process().name)
    # print(rTree.RandomTree.deserialize_all())


def local_bin(file_path, use_tree=None):
    csv_input_file = fReader.FileReader(file_path, True)
    csv_input_file.csv_read()
    if use_tree is None:
        tree = rTree.RandomTree.generate_random_tree()
    else:
        tree = use_tree
    number_of_algorithm = len(csv_input_file.get_line(0))
    random_algorthm = rAlgorithm.random_numers_between(number_of_algorithm,
                                                       rAlgorithm.random_choice(data=3, end=number_of_algorithm - 2),
                                                       star=2)
    i = 0
    f_Measure = fMeasure.FMeasure()
    for line in csv_input_file.get_result():
        new_tree = copy.deepcopy(tree)
        values = [float(line[i]) for i in random_algorthm]
        new_tree.add_data_in_tree(values)
        threshold = new_tree.get_tree_result()
        f_Measure.recalculate_tp_fp_fn_tn_for_local(csv_input_file, i, threshold)
        i += 1
    fMeasure_for_local = f_Measure.calculate_f_measure_for_local()
    # print(fMeasure_for_local)
    return fMeasure_for_local, file_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Pardkraduli Team Project', description='Monte Carlo Tree')
    parser.add_argument('-t', '--type', help='Choose the type of binarization', choices=['global', 'local'])
    parser.add_argument('-s', '--use-saved-best', help='Use the best saved tree. [TODO]', action='store_true')
    parser.add_argument('-g', '--global-file',
                        help='If -t global was given, the path to the Global file input must be specified here')
    parser.add_argument('-l', '--lut-file',
                        help='If -t global was given, the path to the LUT file input must be specified here')
    parser.add_argument('-d', '--local-dir',
                        help='If local is given and you want to check all the files in a directory, you must specify '
                             'the directory here')
    parser.add_argument('-f', '--local-file',
                        help='If -t is given locally and you want to check only one file, the path must be entered here')
    configure_logging()
    cfg = parser.parse_args()
    rTree.RandomTree.deserialize_all()
    best_tree = None
    if cfg.use_saved_best:
        for tr in rTree.RandomTree.deserialize_all():
            if (best_tree == None):
                best_tree = tr
            elif best_tree.score < tr.score:
                best_tree = tr
        print("Used best tree with fMeasure = " , best_tree.score)
    if cfg.type == 'global':
        processes = []
        if (best_tree != None):
            global_bin_use_saved(cfg.lut_file, cfg.global_file, best_tree)
            exit(0)
        for i in range(12):
            p = Process(target=global_bin, args=(cfg.lut_file, cfg.global_file))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()

        # global_bin(cfg.lut_file, cfg.global_file)
    elif cfg.type == 'local':
        calculated_f_measue = 0
        if cfg.local_dir is not None:
            only_files = [join(cfg.local_dir, f) for f in listdir(cfg.local_dir) if isfile(join(cfg.local_dir, f))]
            with concurrent.futures.ProcessPoolExecutor(max_workers=12) as executor:
            # Submit tasks to the pool
                results = [executor.submit(local_bin, file, best_tree) for file in only_files]
                print("Files will be procesed: ", len(results))
                # Wait for all tasks to complete and retrieve the results
                for future in concurrent.futures.as_completed(results):
                    result = future.result()
                    print("Result:", result[0], result[1])
                    calculated_f_measue += result[0]
                print("FMEasure per set:", calculated_f_measue/len(results))
            # for file in only_files:
            #     local_bin(file, use_tree=best_tree)
        elif cfg.local_file is not None:
            local_bin(cfg.local_file, use_tree=best_tree)
        else:
            parser.print_help()
    else:
        parser.print_help()
