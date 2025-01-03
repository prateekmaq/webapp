from flask import Flask, render_template, jsonify
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
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
        "FLASK_APP_NAME": os.getenv('FLASK_APP_NAME'),
        "FLASK_ENV": os.getenv('FLASK_ENV'),
        "FLASK_DEBUG": os.getenv('FLASK_DEBUG'),
        "API_URL": os.getenv('API_URL'),
        "SECRET_KEY": os.getenv('SECRET_KEY')
    }
    return render_template('env.html', env_variables=env_variables)

if __name__ == '__main__':
    app.run(debug=True)
