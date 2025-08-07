from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result")
def result():
    try:
        df = pd.read_csv("clustered_data.csv")
        summary = df.groupby("Cluster").mean().round(2).reset_index()
        return render_template("result.html", tables=[summary.to_html(classes="data", index=False)])
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
