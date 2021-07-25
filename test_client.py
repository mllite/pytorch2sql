
import pickle, json, requests, base64

from sklearn import datasets

iris = datasets.load_iris()
X = iris.data  
Y = iris.target
# print(iris.DESCR)

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier()
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

