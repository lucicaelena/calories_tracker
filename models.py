from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    meal = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    carbs = db.Column(db.Integer, nullable=False)
    proteins = db.Column(db.Integer, nullable=False)
    fat = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Food {self.name} {self.meal} {self.date}>"