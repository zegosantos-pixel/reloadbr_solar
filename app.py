from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    region = request.form.get("region")
    state = request.form.get("state")
    providers = utils.load_providers()

    if region:
        providers = [p for p in providers if p["regiao"].lower() == region.lower()]
    if state:
        providers = [p for p in providers if p["estado"].lower() == state.lower()]

    # ordena pelo menor preço (mais relevante)
    providers = sorted(providers, key=lambda x: float(x["preco_kwh"]))

    return render_template("index.html", providers=providers, region=region, state=state)

if __name__ == "__main__":
    app.run(debug=True)
