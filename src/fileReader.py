import csv

"""
    Read and store a csv file in a matrix without first line if need.
    Class can return full matrix, csv line, csv collumn,
    csv element and print matrix
"""
class FileReader:
    def __init__(self, file_path, need_first_line = False):
        self.file_path = file_path
        self.result = []
        self.need_first_line = need_first_line

    def csv_read(self):
        with open(self.file_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                self.result.append(line)
            if not self.need_first_line:
                self.result = self.result[1:]

    def get_line(self, idx):
        return self.result[idx]

    def get_collumn(self, idx):
        return [linie[idx] for linie in self.result]

    def get_element(self, i, j):
        return float(self.result[i][j])

    def get_result(self):
        return self.result

    def print_result(self):
        for line in self.result:
            print(line)