from testimonials import app
from flask import render_template

testimonials = [
    {
        'id': 10,
        'name': 'Connor',
        'message': 'Your course helped me land a job'
    },
    {
        'id': 35,
        'name': 'Sarah',
        'message': 'Great!'
    },
    {
        'id': 43,
        'name': 'John',
        'message': 'Loved it!'
    }
]


@app.route('/')
def index():
    return render_template('index.html', testimonials=testimonials)


@app.route('/<id>')
def show_testimonial(id):
    for testimonial in testimonials:
        if testimonial.get('id') == int(id):
            return render_template('testimonial.html', testimonial=testimonial)
