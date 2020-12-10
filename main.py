from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is super secret key'


class PostStatusForm(FlaskForm):
    status_field = StringField('Status', validators=[DataRequired()])
    submit = SubmitField('Post')


@app.route('/', methods=['GET', 'POST'])
def homepage():
    data = {
        'name': 'John Smith',
        'image': ''
    }

    form = PostStatusForm()

    if form.validate_on_submit():
        print('You entered {}'.format(form.status_field.data))
        return redirect('/')

    return render_template('home.html', data=data, form=form)


if __name__ == '__main__':
    app.run(debug=True)
