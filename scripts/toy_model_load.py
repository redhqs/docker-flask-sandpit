import pickle

model_save_path = "./models/toy-model.pkl"
with open(model_save_path, 'rb') as file:
    clf = pickle.load(file)

# test iris
X_example = [[5.0, 1.0, 4.0, 2.0]]

y_example = clf.predict(X_example)
print(y_example)
