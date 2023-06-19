import csv

def dictionary_to_csv(d, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y', 'value'])
        for key, value in d.items():
            x, y = key
            writer.writerow([x, y, value])

def force_to_csv(xy_tuple, ab_list,file_name):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(list(xy_tuple) + ab_list)


