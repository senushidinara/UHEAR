from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    stats = {
        "total_users": 1200,
        "scenario_completion": "72%",
        "leaderboard": [
            {"user":"anon_1","points":500},
            {"user":"anon_2","points":450}
        ]
    }
    return render_template("dashboard.html", stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
