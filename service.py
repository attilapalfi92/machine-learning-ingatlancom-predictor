from flask import Flask
from flask import render_template
import constants, sys
from flask import request
from werkzeug.contrib.cache import SimpleCache
from production.housing_price_predictor import HousingPricePredictor
import pandas as pd
from production.geocoder import geocode_address

#cache = SimpleCache()
predictor = HousingPricePredictor(pd.read_csv("data/flats2.csv"))

app = Flask(__name__)

#@app.before_first_request
def custom_call():
    app.logger.debug("Start training")

    initial_dataset = pd.read_csv("data/flats.csv")
    #dataset = initial_dataset.sample(frac=1).reset_index(drop=True)
    predictor = HousingPricePredictor(initial_dataset)

    #app.logger.debug("Predictor size: " + str(sys.getsizeof(predictor)))

    #cache.set('predictor', predictor, 60*60)
    #predictor_cached = cache.get('predictor') #test if None
    #app.logger.debug(predictor_cached)

@app.route('/')
def index():
    building_constants = {
        'mat': constants.BUILDING_MATERIAL,
        'comfort': constants.COMFORT,
        'cond': constants.CONDITION,
        'heating': constants.HEATING,
        'parking': constants.PARKING,
        'sub_type': constants.SUB_TYPE,
        'toilet': constants.TOILET_TYPE,
    }
    return render_template('index.html', props=building_constants)

@app.route('/predict', methods=['POST',])
def hello():
    error = None
    if request.method == 'POST':
        building_levels = request.form['building_levels']
        building_material = request.form['building_material']
        comfort = request.form['comfort']
        cond = request.form['cond']
        floor = request.form['floor']
        heating = request.form['heating']
        parking = request.form['parking']
        rooms_whole = request.form['rooms_whole']
        rooms_half = request.form['rooms_half']
        address = request.form['address']
        size = request.form['size']
        sub_type = request.form['sub_type']
        toilet = request.form['toilet']

        #TODO: debug returned type of rooms
        if rooms_whole == 0:
            rooms = str(rooms_half) + " fél"
        elif rooms_half == 0:
            rooms = str(rooms_whole)
        else:
            rooms = str(rooms_whole) + " + " + str(rooms_half) + " fél"

        parameter_pd = pd.DataFrame()
        parameter_pd['building_levels'] = [building_levels]
        parameter_pd['building_material'] = [building_material]
        parameter_pd['comfort'] = [comfort]
        parameter_pd['cond'] = [cond]
        parameter_pd['floor'] = [floor]
        parameter_pd['heating'] = [heating]
        parameter_pd['parking'] = [parking]
        parameter_pd['rooms'] = [rooms]
        parameter_pd['size'] = [size]
        parameter_pd['sub_type'] = [sub_type]
        parameter_pd['toilet'] = [toilet]

        latlong = geocode_address(address)

        parameter_pd['longitude'] = latlong['longitude']
        parameter_pd['latitude'] = latlong['latitude']
        parameter_pd['location_accuracy'] = ['ROOFTOP']

        prediction = predictor.predict(parameter_pd)
        app.logger.info(prediction)
        print(str(prediction))

    return render_template('prediction.html', prediction=prediction)



if __name__ == '__main__':
    app.run()