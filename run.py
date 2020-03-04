import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

def get_params(form_data):
    dist = form_data.get("dist").lower()
    mean = float(form_data.get("mean"))
    var = float(form_data.get("var"))
    samples = int(form_data.get("samples"))
    return dist, mean, var, samples

@app.route("/random_numbers", methods=["GET", "POST"])
def random_numbers():
    if request.method == "POST":
        dist, mean, var, samples = get_params(request.form)
        dist_func = np.random.normal if dist == "n" else np.random.lognormal
        rand_num_list = dist_func(mean, var, samples).tolist()
        return render_template("app.html",
                               rand_num_list=rand_num_list,
                               dist=dist,
                               mean=mean,
                               var=var,
                               samples=samples)
    else:
        return render_template("app.html")


app.run(host="localhost", port=5000)