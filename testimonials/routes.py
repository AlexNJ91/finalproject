from testimonials import app, db
from flask import render_template, abort, jsonify
from testimonials.models import Testimonial


testimonials = [
    {
        'id': 10,
        'name': 'Connor',
        'message': 'Your course helped me get a job'
    },
    {
        'id': 35,
        'name': 'Sarah',
        'message': 'Great!'
    }
    ]


@app.route('/api/testimonials')
def get_testimonials():
    testimonials = Testimonial.query.all()
    return jsonify({'testimonials': testimonials})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404 NOT FOUND"), 404


@app.route('/')
def index():
    return render_template('index0.html')


@app.route('/testimonials')
def show_testimonials():
    return render_template('index.html', testimonials=testimonials)


@app.route('/testimonials/<id>')
def show_testimonial(id):
    for testimonial in testimonials:
        if testimonial.get('id') == int(id):
            return render_template('testimonial.html', testimonial=testimonial)
    abort(404)
