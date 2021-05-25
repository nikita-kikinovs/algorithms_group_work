# python version: 3
import csv

# path to folder with processable files
path_to_folder = '/Users/nikitakikinovs/Downloads/Graphs/'
# array with file names
file_names = ['karate.csv', 'miserables-edges.csv', 'miserables-nodes.csv']

for file_name in file_names:
    with open(path_to_folder + file_name, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    print(data)
    print("\n\n\n")
