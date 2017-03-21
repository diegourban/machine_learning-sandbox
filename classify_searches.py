import pandas as pd
from collections import Counter

# Loading data frame
data_frame = pd.read_csv('search.csv')

X_df = data_frame[['home', 'busca', 'logado']]
Y_df = data_frame['comprou']

# Processing the dummies(transforming the column busca to binary category)
Xdummies_df = pd.get_dummies(X_df).astype(int)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

# Separating training and test data
training_percentage = 0.9

training_size = int(training_percentage * len(Y))
training_data = X[:training_size]
training_markings = Y[:training_size]

test_size = len(Y) - training_size
test_data = X[-test_size:]
test_markings = Y[-test_size:]

# Training
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(training_data, training_markings)

# Evaluating algorithm efficiency
result = model.predict(test_data)
hits = (result == test_markings)
total_hits = sum(hits)
total_elements = len(test_data)
hit_rate = 100.0 * total_hits / total_elements
print ("Algorithm hit rate: %f" % hit_rate)
print ("Total test elements: %d" % total_elements)

# Evaluating dumb(0 or 1) algorithm efficiency
base_hits = max(Counter(test_markings).itervalues())
base_hit_rate = 100.0 * base_hits / len(test_markings)
print ("Base hit rate: %f" % base_hit_rate)
