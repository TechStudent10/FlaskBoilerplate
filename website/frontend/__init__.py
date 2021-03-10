from flask import Blueprint, render_template

frontend = Blueprint(
    'frontend',
    __name__,
    template_folder="frontend\\templates",
    static_folder="frontend\\static"
)

@frontend.route('/')
def index():
    return render_template('index.html')

@frontend.route('/about')
def about():
    return render_template('about.html')