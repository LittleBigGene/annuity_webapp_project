import numpy as np
import pandas as pd
from flask import Flask, request, render_template

from src.discount_curve_module import DiscountCurveProvider
from src.number_crunching_modules import NumberCruncher
from src.swap_rate_module import SwapRateProvider

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
        mort_tables = pd.read_csv('./src/mortality.csv')
        try:
            swap = SwapRateProvider().get_swap_from_csv()
            dcp = DiscountCurveProvider(tenors = swap['Tenor'], parcurve = swap['Swap'], extrap_yrs = 90)
            qx = mort_tables[sex.upper()].values
            nc = NumberCruncher(age, sex, payment, qx, dcp.bootstrap())   
            price = nc.actuarial_PV()
        except:
            price = 0

        return render_template("app.html",
                               age = age,
                               sex = sex,
                               payment = payment,
                               result = price.round(2)
                               )
    else:
        return render_template("app.html")

if __name__=='__main__':
    app.run(host="localhost", port=5000)