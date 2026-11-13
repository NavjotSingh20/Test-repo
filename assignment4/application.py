import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "development")
    message = os.getenv("APP_MESSAGE", "Hello from Elastic Beanstalk!")

    return f"""
    <html>
        <head><title>Assignment 4 - Elastic Beanstalk</title></head>
        <body style="font-family: Arial; text-align: center; padding: 60px;">
            <h1>AWS Elastic Beanstalk Deployment</h1>
            <h2>{message}</h2>
            <p>Environment: {environment}</p>
            <p>Deployment Version: 1.0</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)