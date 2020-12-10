from flask import Flask, render_template, redirect, request, render_template_string
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is super secret key'


class PostStatusForm(FlaskForm):
    status_field = StringField('Status', validators=[DataRequired()])
    submit = SubmitField('Post')

class Post:
    def __init__(self, text, date):
        self.text = text
        self.date = date

posts = [
    Post('This is my first post', '2019-12-10'),
    Post('Random text for this post', '2020-10-10'),
    Post('This is awesome app', '2020-1-10')
]


@app.route('/', methods=['GET', 'POST'])
def homepage():
    data = {
        'name': 'John Smith',
        'posts': posts
    }

    form = PostStatusForm()

    if form.validate_on_submit():
        posts.append(Post(form.status_field.data, date.today()))
        return redirect('/')

    template = '''
        {% include "home.html" %}
        <h3>See whats new</h3>
    '''

    for post in data['posts']:
        post_html = '''
            <p>{}</p>
            <p>{}</p>
        '''.format(post.text, post.date)

        template += post_html

    return render_template_string(template, data=data, form=form)


if __name__ == '__main__':
    app.run(debug=True)
