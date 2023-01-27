from flask import Flask, request
import pickle
from numpy import array2string

model_save_path = "./models/toy-model.pkl"
with open(model_save_path, 'rb') as file:
    clf = pickle.load(file)

# define app
app = Flask(__name__)

# define functions to be called
@app.route("/score", methods=["POST", "GET"])
def predict_species():
    flower = []
    flower.append(request.args.get("petal_length"))
    flower.append(request.args.get("petal_width"))
    flower.append(request.args.get("sepal_length"))
    flower.append(request.args.get("sepal_width"))
    return array2string(clf.predict([flower]))

# define main
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5001")
