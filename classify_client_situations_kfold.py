from collections import Counter
from sklearn.cross_validation import cross_val_score
import pandas as pd
import numpy as np

# Loading data frame
data_frame = pd.read_csv('data/client_situation.csv')

X_df = data_frame[['recencia', 'frequencia', 'semanas_de_inscricao']]
Y_df = data_frame['situacao']

# Processing the dummies(transforming the column busca to binary category)
Xdummies_df = pd.get_dummies(X_df).astype(int)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

# Separating training, test and validation data
training_percentage = 0.8

training_size = int(training_percentage * len(Y))

training_data = X[0:training_size]
training_markings = Y[0:training_size]

validation_data = X[training_size:]
validation_markings = Y[training_size:]

print ("Total training and test elements: %d" % len(training_data))
print ("Total validation elements: %d" % len(validation_data))

def fit_and_predict(name, model, training_data, training_markings):
    k = 10
    scores = cross_val_score(model, training_data, training_markings, cv = k)
    hit_rate = np.mean(scores)
    print "Hit rate of {0}: {1}".format(name, hit_rate)
    return hit_rate

results = {}

# Training and testing multiclass category with OneVsRestClassifier(using LinearSVC)
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
oneVsRest_model = OneVsRestClassifier(LinearSVC(random_state = 0))
oneVsRest_result = fit_and_predict("OneVsRest", oneVsRest_model, training_data, training_markings)
results[oneVsRest_result] = oneVsRest_model

# Training and testing multiclass category with OneVsOneClassifier(using LinearSVC)
from sklearn.multiclass import OneVsOneClassifier
oneVsOne_model = OneVsOneClassifier(LinearSVC(random_state = 0))
oneVsOne_result = fit_and_predict("OneVsOne", oneVsRest_model, training_data, training_markings)
results[oneVsOne_result] = oneVsOne_model

# Training and testing with MultinomialNB
from sklearn.naive_bayes import MultinomialNB
multinomial_model = MultinomialNB()
multinomial_result = fit_and_predict("MultinomialNB", multinomial_model, training_data, training_markings)
results[multinomial_result] = multinomial_model

# Training and testing with AdaBoostClassifier
from sklearn.ensemble import AdaBoostClassifier
adaboost_model = AdaBoostClassifier()
adaboost_result = fit_and_predict("AdaBoostClassifier", adaboost_model, training_data, training_markings)
results[adaboost_result] = adaboost_model

# Choosing the winner
maximum = max(results)
winner_model = results[maximum]

# Validating the winner
winner_model.fit(training_data, training_markings)
result = winner_model.predict(validation_data)
hits = (result == validation_markings)
total_hits = sum(hits)
total_elements = len(validation_data)
hit_rate = 100.0 * total_hits / total_elements
print ("Winner algorithm validation hit rate: %f" % hit_rate)

# Evaluating dumb algorithm efficiency
base_hits = max(Counter(validation_markings).itervalues())
base_hit_rate = 100.0 * base_hits / len(validation_markings)
print ("Base test hit rate: %f" % base_hit_rate)
