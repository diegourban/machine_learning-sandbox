from data_loader import load_accesses

X, Y = load_accesses()

# Approach: To evaluate your model, train it with 90% of the input and test with the other 10%
# Extracting first 90 elements for training
training_data = X[:90]
training_markings = Y[:90]

# Extracting last 9 elements for testing
test_data = X[-9:]
test_markings = Y[-9:]

# Training the model with the 90%
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(training_data, training_markings)

# Testing and evaluating the hit rate with the 10%
result = model.predict(test_data)
differences = result - test_markings
hits = [d for d in differences if d == 0]
total_hits = len(hits)
total_elements = len(test_data)
hit_rate = 100.0 * total_hits / total_elements
print (hit_rate)
print (total_elements)

'''
With the hit rate we can measure how good is our algorithm.
If the hit rate is high, it predicted most cases right.
If the hit rate is low, we must evaluate our tests
'''
