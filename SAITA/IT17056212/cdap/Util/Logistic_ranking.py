import pandas as pd
from sklearn.linear_model import LogisticRegression
from Data.Variables import *


class Logistic:

    def ranking(self, predict_array):
        # Importing the dataset
        dataset = pd.read_csv(issue_history_csv)
        X = dataset.iloc[:, [0, 1, 2]].values
        y = dataset.iloc[:, 3].values

        model = LogisticRegression(random_state=0, max_iter=400)
        model.fit(X, y)

        import pickle

        filename = '../Data/rank_model.sav'
        pickle.dump(model, open(filename, 'wb'))

        # load the model from disk
        loaded_model = pickle.load(open(filename, 'rb'))

        # Predicting the  results
        y_pred = loaded_model.predict([predict_array])
        print(y_pred)
        return y_pred
