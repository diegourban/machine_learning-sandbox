import csv

def load_accesses():
    X = [] # data
    Y = [] # markings

    csv_file = open('access.csv', 'rb')
    csv_reader = csv.reader(csv_file)

    csv_reader.next() # skipping the first line

    for home, how_it_works, contact, bought in csv_reader:
        data = [int(home), int(how_it_works), int(contact)]
        X.append(data)
        Y.append(int(bought))

    return X, Y

def load_searches():
    X = []
    Y = []

    csv_file = open('search.csv', 'rb')
    csv_reader = csv.reader(csv_file)
    csv_reader.next()

    for home, busca, logado, comprou in csv_reader:
        data = [int(home), busca, int(logado)]
        X.append(data)
        Y.append(int(comprou))

    return X,Y  
