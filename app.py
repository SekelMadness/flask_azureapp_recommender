from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_recommendations(user_id):
    function_url = "https://myrecommenderfunctionappserverless.azurewebsites.net/api/recommend_article"
    params = {"userID": user_id}
    response = requests.get(function_url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        return "Error fetching recommendations"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        if user_id:
            recommendations = get_recommendations(user_id)
            return render_template("result.html", recommendations=recommendations)
        else:
            return "Please enter a User ID."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    