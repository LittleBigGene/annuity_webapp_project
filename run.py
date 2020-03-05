import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from src.discount_curve_module import DiscountCurveProvider

app = Flask(__name__)

def get_params(form_data):
    try:
        age = int(form_data.get("age"))
    except:
        age = 65
    try:
        sex = str(form_data.get("sex"))
    except:
        sex = 'm'
    try:
        payment = float(form_data.get("payment"))
    except:
        payment = 2000
    return age, sex, payment

@app.route("/", methods=["GET", "POST"])
def annunity_price():
    if request.method == "POST":
        age, sex, payment = get_params(request.form)
        swap = pd.read_csv('./src/swaps.csv')
        dcp = DiscountCurveProvider(tenors = swap['Tenor'], parcurve = swap['Swap'])
            
        try:
            price = dcp.bootstrap()[0]
        except:
            price = 0

        return render_template("app.html",
                               age = age,
                               sex = sex,
                               payment = payment,
                               result = price
                               )
    else:
        return render_template("app.html")

if __name__=='__main__':
    app.run(host="localhost", port=5000)