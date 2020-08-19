import pickle
import json

with open('../Data/paragraph_data.json') as f:
    data_dict = json.load(f)

print(data_dict)

with open('../Data/data_pkl.pkl', 'wb') as pickle_file:
    pickle.dump(data_dict, pickle_file)
