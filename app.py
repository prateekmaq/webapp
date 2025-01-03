from flask import Flask, render_template, jsonify
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "dummy_secret_key"
api_url = "https://randomuser.me/api"

def fetch_users(num_users=30):
    url = f"{api_url}?results={num_users}"
    response = requests.get(url)
    return response.json()['results']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/users')
def get_users():
    users = fetch_users()
    return jsonify(users)

@app.route('/env')
def display_env():
    env_variables = {
        "FLASK_APP_NAME": "dummy_flask_app_name",
        "FLASK_ENV": "dummy_flask_env",
        "FLASK_DEBUG": "dummy_flask_debug",
        "API_URL": "https://dummyapi.com",
        "SECRET_KEY": "dummy_secret_key"
    }
    return render_template('env.html', env_variables=env_variables)

if __name__ == '__main__':
    app.run(debug=True)
