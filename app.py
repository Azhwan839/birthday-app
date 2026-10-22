from flask import Flask, render_template, request

app = Flask("app")

@app.route('/')
@app.route('/<name>')
def birthday(name=None):
    if name is None:
        name = request.args.get('name', 'دوست عزیز')
    return render_template('birthday.html', name=name)

app.run(debug=True)