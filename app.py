# Import all the flask related functions
from flask import Flask, render_template, request,redirect
# Import the database object which is initialized in the models module
from models import db, Food
from datetime import date
from datetime import datetime
# Initialize a Flask object on which we can write routes
app = Flask(__name__)

# We configure the SQLALCHEMY Database location
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///calories.db"

# We initialize the database connection
db.init_app(app)
@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/log_food")
def home():
    day = request.args.get('day')

    # The first request should show the data for today
    if not day:
        day = date.today()

    breakfast_food = Food.query.filter_by(date=day, meal='breakfast').all()
    lunch_food = Food.query.filter_by(date=day, meal='lunch').all()
    dinner_food = Food.query.filter_by(date=day, meal='dinner').all()

    total_calories = 0
    breakfast_calories = 0
    lunch_calories = 0
    dinner_calories = 0

    for food in breakfast_food:
        breakfast_calories += food.calories
        total_calories += food.calories

    for food in lunch_food:
        lunch_calories += food.calories
        total_calories += food.calories

    for food in dinner_food:
        dinner_calories += food.calories
        total_calories += food.calories

    calories_day = 3500
    calories_remaining = calories_day - total_calories

    return render_template("hello.html",
                           breakfast_food=breakfast_food,
                           lunch_food=lunch_food,
                           dinner_food=dinner_food,
                           day=day,
                           breakfast_calories=breakfast_calories,
                           lunch_calories=lunch_calories,
                           dinner_calories=dinner_calories,
                           total_calories=total_calories,
                           calories_day=calories_day,
                           calories_remaining=calories_remaining
                           )

@app.route("/add_food/", methods=["GET", "POST"])
def add_food():
    date_obj = datetime.now().date()
    if request.method == 'GET':
        return render_template('add_food.html')
    elif request.method == 'POST':
        food = Food(
            name=request.form['name'],
            meal=request.form['meal'],
            calories=request.form['calories'],
            carbs=request.form['carbs'],
            proteins=request.form['proteins'],
            fat=request.form['fat'],
            date=date_obj

        )
        print(request.form['name'],)
        print(request.form['meal'])
        db.session.add(food)
        db.session.commit()
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)