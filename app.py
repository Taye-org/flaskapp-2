from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Keep going, you're getting there!",
    "Progress over perfection.",
    "Discomfort is the price of growth.",
    "You're doing better than you think.",
    "Don’t stop now — you’re closer than ever.",
    "Discipline > Motivation.",
    "Consistency builds confidence."
]

@app.route('/')
def random_quote():
    return jsonify({
        "quote": random.choice(quotes),
        "source": "flask-app-2"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
