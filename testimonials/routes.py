from testimonials import app
from flask import render_template

testimonials = [
    {
        'id': 10,
        'name': 'Connor',
        'message': 'Your course helped me land a job'
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
