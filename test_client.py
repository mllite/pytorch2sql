
import pickle, json, requests, base64

from sklearn import datasets



import torch
from torch import nn
import torch.nn.functional as F

import skorch
from skorch import NeuralNetClassifier

torch.manual_seed(1960)

torch.set_default_tensor_type('torch.DoubleTensor')



def create_model():
    hidden_units = 15
    num_classes = 3
    num_inputs = 4
    model = nn.Sequential(
        nn.Linear(num_inputs, hidden_units),
        nn.ReLU(),
        nn.Dropout(),
        nn.Linear(hidden_units , num_classes),
        nn.Softmax())

    return model

iris = datasets.load_iris()
X = iris.data  
Y = iris.target
# print(iris.DESCR)

clf = skorch.NeuralNetClassifier(
    create_model(),
    optimizer=torch.optim.Adam,
    max_epochs=10,
)


print(X.shape , Y.shape)
clf.fit(X, Y)

def test_ws_sql_gen(pickle_data):
    WS_URL="https://sklearn2sql.herokuapp.com/model"
    # WS_URL="http://localhost:1888/model"
    b64_data = base64.b64encode(pickle_data).decode('utf-8')
    data={"Name":"model1", "PickleData":b64_data , "SQLDialect":"postgresql"}
    r = requests.post(WS_URL, json=data)
    # r.raise_for_status()
    content = r.json()
    # print(content.keys())
    # print(content)
    lSQL = content["model"]["SQLGenrationResult"][0]["SQL"]
    return lSQL;


pickle_data = pickle.dumps(clf)
lSQL = test_ws_sql_gen(pickle_data)
print(lSQL)

