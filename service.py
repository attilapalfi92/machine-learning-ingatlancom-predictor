from flask import Flask
from flask import render_template
import constants, os
from flask import request
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

app = Flask(__name__)


class TempObject:
    def __init__(self):
        self.somekey = "somevalue"

@app.before_first_request
def custom_call():
    app.logger.debug("Starting custom call")

    predictor = TempObject()

    cache.set('predictor', predictor, 60*60)
    predictor_cached = cache.get('predictor') #test if None
    app.logger.debug(predictor_cached)

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

        pass
    predictor = cache.get('predictor')

    prediction=None
    return render_template('prediction.html', prediction=prediction)



if __name__ == '__main__':
    app.run()