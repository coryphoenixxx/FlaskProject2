from flask import Flask, render_template

import random
import data


app = Flask(__name__)

tours = data.tours


@app.route('/')
@app.route('/index/')
@app.route('/main/')
def render_main():
    random_tours = list(tours.keys())
    random.shuffle(random_tours)
    return render_template('index.html', data=data, random_tours=random_tours[:6])


@app.route('/departures/<departure>/')
def render_departure(departure):
    count = 0
    prices, nights = [], []
    for tour in tours.values():
        if tour['departure'] == departure:
            count += 1
            prices.append(tour['price'])
            nights.append(tour['nights'])
    info = (count, min(prices), max(prices), min(nights), max(nights))
    return render_template("departure.html", data=data, departure=departure, info=info)


@app.route('/tours/<id>/')
def render_tour(id):
    return render_template("tour.html", data=data, id=int(id))


if __name__ == '__main__':
    app.run()
