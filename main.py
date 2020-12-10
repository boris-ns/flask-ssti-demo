from flask import Flask, request, render_template_string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is super secret key for JWT'


@app.route("/")
def index():
    search = request.args.get('search') or None

    template = '''
        <p>Hello world</p>
        {}
    '''.format(search)

    return render_template_string(template)

if __name__ == '__main__':
    app.run()
