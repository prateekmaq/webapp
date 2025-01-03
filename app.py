from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://randomuser.me/api/?results=30')
    users = response.json()['results']
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
