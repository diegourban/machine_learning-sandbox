import csv

def load_accesses():
    X = [] # data
    Y = [] # markings

    csv_file = open('../data/access.csv', 'rb')
    csv_reader = csv.reader(csv_file)

    csv_reader.next() # skipping the first line

    for home, how_it_works, contact, bought in csv_reader:
        data = [int(home), int(how_it_works), int(contact)]
        X.append(data)
        Y.append(int(bought))

    return X, Y
