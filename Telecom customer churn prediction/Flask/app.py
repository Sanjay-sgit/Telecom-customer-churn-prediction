from flask import Flask, render_template, request
import keras
from keras.models import load_model

app = Flask(__name__)
model = load_model("bank_churn.h5")


@app.route('/')
def helloworld():
    return render_template('base.html')


@app.route('/assesment')
def prediction():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def admin():
    a = request.form["Country"]
    if a == 'france':
        a1, a2, a3 = 1, 0, 0
    elif a == 'germany':
        a1, a2, a3 = 0, 1, 0
    elif a == 'spain':
        a1, a2, a3 = 0, 0, 1
    b = request.form["Gender"]
    if b == 'm':
        b1, b2 = 0, 1
    elif b == 'f':
        b1, b2 = 1, 0
    c = int(request.form["Credit_Score"])
    d = int(request.form["Age"])
    e = int(request.form["Tenure"])
    f = int(request.form["Balance"])
    g = int(request.form["NumOfProducts"])
    h = request.form["HasCreditCard"]
    if h == "y":
        h = 1
    if h == "n":
        h = 0
    i = request.form["IsActiveMember"]
    if (i == "y"):
        i = 1
    if (i == "n"):
        i = 0
    j = float(request.form['EstimatedSalary'])
    k = [[a1, a2, a3, b1, b2, c, d, e, f, g, h, i, j]]
    print(k)
    x = model.predict(k)
    print(x[0])
    if x[0] <= 0.5:
        y = "N0"
        return render_template("predno.html", z=y)
    elif x[0] >= 0.5:
        y = "Yes"
        return render_template("predyes.html", z=y)


if __name__ == '__main__':
    app.run(debug=True)
