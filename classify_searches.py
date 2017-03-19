import pandas as pd

data_frame = pd.read_csv('search.csv')

X_df = data_frame[['home', 'busca', 'logado']]
Y_df = data_frame['comprou']

# processing the dummies(transforming the column busca to binary category)
Xdummies_df = pd.get_dummies(X_df).astype(int)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

training_percentage = 0.9

training_size = int(training_percentage * len(Y))
training_data = X[:training_size]
training_markings = Y[:training_size]

test_size = len(Y) - training_size
test_data = X[-test_size:]
test_markings = Y[-test_size:]

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(training_data, training_markings)

result = model.predict(test_data)
differences = result - test_markings
hits = [d for d in differences if d == 0]
total_hits = len(hits)
total_elements = len(test_data)
hit_rate = 100.0 * total_hits / total_elements
print (hit_rate)
print (total_elements)
