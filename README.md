# 🔢Number Guessing App using Flask of Python

🌟A Flask application where the user can enter the number to guess in the URL and according to the conditions set in program, the respective page gets rendered. This 
program builds the basic understanding and usecase of Flask server and its decorator functions to render web pages.

👉In the 'main.py' file, first a random number between 0 to 9 is generated using the random module which is stored in a variable for reference.

👉Next, using the Flask decorator function, the home route is setup which contains a simple h1 and a gif in imag tag creating the user interface.

![Home Route](https://github.com/bellaryyash23/Higher_Lower_Flask/blob/master/samples/start.JPG?raw=true)

👆Home Route👆

👉Now, using Flask we create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" and checks that number against the generated random number.
If the number is too low, tell the user it's too low, same with too high or if they found the correct number.

👉For example:) If the random number was 6 then,

👉Now, if user entered 5 in the url i.e. URL/5, then the following page gets rendered with the message suggesting the number is lower than actual number.

![Low Route](https://github.com/bellaryyash23/Higher_Lower_Flask/blob/master/samples/low.JPG?raw=true)

👆Route if number is Lower than actual number👆

👉If the user entered 7 in the url i.e. URL/7, then page suggesting that number is higher than actual number is rendered.

![Route for Higher Number](https://github.com/bellaryyash23/Higher_Lower_Flask/blob/master/samples/high.JPG?raw=true)

👆Route if number is Higher than actual number👆

👉Finally if the user entered 6 i.e. URL/6 which is the right anwer then the page with that message gets rendered.

![Route for Correct Answer Number](https://github.com/bellaryyash23/Higher_Lower_Flask/blob/master/samples/ans.JPG?raw=true)

👆Route for the Correct Answer number👆
