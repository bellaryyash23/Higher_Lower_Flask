from flask import Flask
import random

app = Flask(__name__)
ran_num = random.randint(0, 9)


@app.route("/")
def home():
    return "<h1 style='color:blue'>Guess a number between 0 to 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route("/<int:num>")
def page(num):
    if num > ran_num:
        return "<h1 style='color:red'>Too High, try again !</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"
    elif num < ran_num:
        return "<h1 style='color:orange'>Too Low, try again !</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>"
    elif num == ran_num:
        return "<h1 style='color:green'>YOU FOUND ME!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"


if __name__ == "__main__":
    app.run(debug=True)
