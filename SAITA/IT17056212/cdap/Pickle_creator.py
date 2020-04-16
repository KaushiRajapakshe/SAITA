import pickle

data_dict = {
    'restart': 'Restating-service is recomanded. Restarting-Service is a good solution when solving service and registry relaated issues. Restarting-Service can be achieved through',

}

with open('data_pkl.pkl', 'wb') as pickle_file:
    pickle.dump(data_dict, pickle_file)

