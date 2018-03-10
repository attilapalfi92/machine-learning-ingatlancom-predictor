from flask import Flask
from flask import render_template
import constants

app = Flask(__name__)


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

@app.route('/predict')
def hello():
    return 'Hello, World'



if __name__ == '__main__':
    app.run()