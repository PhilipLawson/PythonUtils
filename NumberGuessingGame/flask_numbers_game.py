"""
Re-worded numbers game from numberguess.py in order to work within the flask app framework
"""

from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# Random number to guess
target_number = random.randint(1, 100)
target_range = [1, 100]
num_of_tries = [0]


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        guess = int(request.form["guess"])
        num_of_tries[0] += 1
        if guess in range(target_range[0], target_range[1]):
            if guess < target_number:
                message = "Too low!"
                target_range[0] = guess
            elif guess > target_number:
                message = "Too high!"
                target_range[1] = guess
            else:
                message = f"Congratulations! You guessed the number in {num_of_tries[0]} tries!"
        else:
            message = f"Please enter a number between {target_range[0]} and {target_range[1]}."
    return render_template_string('''
        <html>
            <body>
                <h1>Guess the Number</h1>
                <p>{{ message }}</p>
                <p>Guess within range of <b>{{ target_range[0] }}</b> and <b>{{ target_range[1] }}</b></p>
                <form method="POST">
                    <input type="number" name="guess" min="1" max="100">
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    ''', message=message, target_range=target_range)


if __name__ == "__main__":
    app.run(debug=False)