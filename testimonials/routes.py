from testimonials import app
from flask import render_template


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/api/testimonials')
def testimonials():
    return {'testimonial': ["great", "ok"]}
