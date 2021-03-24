from testimonials import app, db, bcrypt, jwt
from flask import render_template, abort, jsonify, request, make_response
from testimonials.models import Testimonial, User
from flask_jwt_extended import jwt_required, create_access_token
import datetime


@app.route('/')
def index():
    return render_template('index0.html')


@app.route('/login')
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user:
        return {'error': 'username or password incorrect'}, 400

    if bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity={'username': username})
        return {'access_token': access_token}

    else:
        return {'error': 'username or password incorrect'}, 400


@app.route('/api/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify(user.id)


testimonials = [
    {
        'id': 10,
        'name': 'Conor',
        'message': 'Alex has been great to work with. He was a pleasure to train in business development and an asset to the company'
    },
    {
        'id': 35,
        'name': 'Sarah',
        'message': 'Alex was a great ambassador to the company and the ideas he brought to the table really drove us forward'
    },
    {
        'id': 35,
        'name': 'Joanne',
        'message': 'We will be sad to see Alex leave. He has been a key member of our team and we wish him all the best'
    }
    ]


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404 NOT FOUND"), 404


@app.route('/testimonials')
def show_testimonials():
    return render_template('index.html', testimonials=testimonials)


@app.route('/testimonials/<id>')
def show_testimonial(id):
    for testimonial in testimonials:
        if testimonial.get('id') == int(id):
            return render_template('testimonial.html', testimonial=testimonial)
    abort(404)
