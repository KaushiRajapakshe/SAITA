import pickle
import json

# Read JSON file and create a dictionary
with open('../Data/paragraph_data.json') as f:
    data_dict = json.load(f)

print(data_dict)
# Create a pickle file
with open('../Data/data_pkl.pkl', 'wb') as pickle_file:
    pickle.dump(data_dict, pickle_file)
