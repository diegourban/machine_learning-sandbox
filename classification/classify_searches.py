import pandas as pd
from collections import Counter

# Loading data frame
data_frame = pd.read_csv('../data/search.csv')

X_df = data_frame[['home', 'busca', 'logado']]
Y_df = data_frame['comprou']

# Processing the dummies(transforming the column busca to binary category)
Xdummies_df = pd.get_dummies(X_df).astype(int)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

# Separating training, test and validation data
training_percentage = 0.8
test_percentage = 0.1

training_size = int(training_percentage * len(Y))
test_size = int(test_percentage * len(Y))
validation_size = len(Y) - training_size - test_size

training_data = X[0:training_size]
training_markings = Y[0:training_size]
end_training = (training_size + test_size)

test_data = X[training_size:end_training]
test_markings = Y[training_size:end_training]
end_test = training_size + test_size

validation_data = X[end_test:]
validation_markings = Y[end_test:]

print ("Total training elements: %d" % len(training_data))
print ("Total test elements: %d" % len(test_data))
print ("Total validation elements: %d" % len(validation_data))

def fit_and_predict(name, model, training_data, training_markings, test_data, test_markings):
    model.fit(training_data, training_markings)

    # Evaluating algorithm efficiency
    result = model.predict(test_data)
    hits = (result == test_markings)
    total_hits = sum(hits)
    total_elements = len(test_data)
    hit_rate = 100.0 * total_hits / total_elements
    print ("Algorithm test hit rate: {0}: {1}".format(name,  hit_rate))
    return hit_rate



# Training and testing with MultinomialNB
from sklearn.naive_bayes import MultinomialNB
multinomial_model = MultinomialNB()
multinomial_result = fit_and_predict("MultinomialNB", multinomial_model, training_data, training_markings, test_data, test_markings)

# Training and testing with AdaBoostClassifier
from sklearn.ensemble import AdaBoostClassifier
adaboost_model = AdaBoostClassifier()
adaboost_result = fit_and_predict("AdaBoostClassifier", adaboost_model, training_data, training_markings, test_data, test_markings)

# Choosing winner
if multinomial_result > adaboost_result:
    winner_model = multinomial_model
else:
    winner_model = adaboost_model

# Validating the winner
result = winner_model.predict(validation_data)
hits = (result == validation_markings)
total_hits = sum(hits)
total_elements = len(validation_data)
hit_rate = 100.0 * total_hits / total_elements
print ("Winner algorithm validation hit rate: %f" % hit_rate)

# Evaluating dumb(0 or 1) algorithm efficiency
base_hits = max(Counter(validation_markings).itervalues())
base_hit_rate = 100.0 * base_hits / len(validation_markings)
print ("Base test hit rate: %f" % base_hit_rate)
