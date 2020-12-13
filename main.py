from datetime import date

from flask import Flask, render_template, redirect, request, render_template_string
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is super secret key'


class PostStatusForm(FlaskForm):
    status_field = StringField('Create new status', validators=[DataRequired()])
    submit = SubmitField('Post')


class Post:
    def __init__(self, text, date, user):
        self.text = text
        self.date = date
        self.user = user


homepage_posts = [
    Post('This is my first post', '2019-12-10', 'Jane Doe'),
    Post('Random text for this post', '2020-10-10', 'John Doe'),
    Post('This is awesome app', '2020-1-10', 'Will Smith')
]

my_posts = [
    Post('This is awesome app', '2020-1-10', 'John Smith'),
    Post('Hello world!', '2020-1-10', 'John Smith')
]


@app.route('/', methods=['GET', 'POST'])
def homepage():
    data = {
        'name': 'John Smith',
        'posts': my_posts + homepage_posts
    }

    form = PostStatusForm()

    if form.validate_on_submit():
        my_posts.insert(0, Post(form.status_field.data, date.today(), 'John Smith'))
        return redirect('/')

    template = '''
        {% include "home.html" %}
        <div class="template">
        <h3>See whats new</h3>
    '''

    for post in data['posts']:
        post_html = '''
            <span class="post-user">{}</span> -- <span class="post-date">{}</span>
            <p>{}</p>
            <br />
        '''.format(post.user, post.date, post.text)

        template += post_html
    template += "</div>"

    return render_template_string(template, data=data, form=form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    data = {
        'name': 'John Smith',
        'about': 'Hey all, welcome to my profile!',
        'posts': my_posts
    }

    form = PostStatusForm()

    if form.validate_on_submit():
        my_posts.insert(0, Post(form.status_field.data, date.today(), 'John Smith'))

    return render_template('profile.html', data=data, form=form)


@app.errorhandler(404)
def page_not_found(e):
    template = '''
        <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>%s</h3>
        </div>
    ''' % request.url

    return render_template_string(template), 404


if __name__ == '__main__':
    app.run(debug=True)
