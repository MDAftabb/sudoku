import json
from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Load all 60 puzzles once, when the server starts
BASE_DIR = Path(__file__).parent
with open(BASE_DIR / "puzzles.json") as f:
    PUZZLES = json.load(f)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/play")
def play():
    return render_template("play.html")


@app.route("/api/puzzle")
def get_puzzle():
    difficulty = request.args.get("difficulty", "easy").lower()
    number = request.args.get("number", 1, type=int)

    if difficulty not in PUZZLES:
        return jsonify({"error": "Unknown difficulty"}), 400

    total = len(PUZZLES[difficulty])
    if not 1 <= number <= total:
        return jsonify({"error": f"Puzzle number must be 1 to {total}"}), 400

    entry = PUZZLES[difficulty][number - 1]
    return jsonify({
        "difficulty": difficulty,
        "number": number,
        "total": total,
        "puzzle": entry["puzzle"],
        "solution": entry["solution"],
    })


if __name__ == "__main__":
    app.run(debug=True)



    