# Pig or Dog classification

# Defining the data as markings
# [is it fat?, does it have short leg?, does it barks?]
pig1 = [1, 1, 0]
pig2 = [1, 1 ,0]
pig3 = [1, 1 ,0]
dog1 = [1, 1, 1]
dog2 = [0, 1, 1]
dog3 = [0, 1, 1]
data = [pig1, pig2, pig3, dog1, dog2, dog3]
markings = [1, 1, 1, -1, -1, -1]

# Training
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(data, markings)

# Testing some misterious animal
mistery1 = [1, 1, 1]
mistery2 = [1, 0, 0]
mistery3 = [0, 0, 1]
tests = [mistery1, mistery2, mistery3]
test_markings = [-1, 1, -1]

result = model.predict(tests)
print (result)

# Calculating the differences between the result and the expected
differences = result - test_markings
print (differences)

# Percentage of hit rate
hits = [d for d in differences if d == 0]
total_hits = len(hits)
total_tests = len(tests)
hit_rate = 100.0 * total_hits / total_tests
print(hit_rate)
