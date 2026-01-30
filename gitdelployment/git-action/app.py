from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h2>Python Application Deployment</h2>
    <p>Hello from Python to devops community you are doing good keep working </p>
    <p>Status : Application is running</p>
    <p>Deployed using : GitHub Actions</p>
    <p>Time : {datetime.datetime.now()}</p>
    """

if __name__ == "__main__":
    # Make it accessible publicly
    app.run(host='0.0.0.0', port=5000)
