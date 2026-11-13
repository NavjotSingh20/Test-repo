
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "development")
    message = os.getenv(
        "APP_MESSAGE",
        "Hello from Elastic Beanstalk!"
    )

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Assignment 4 - Elastic Beanstalk</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #eef2f7;
                text-align: center;
                padding: 60px;
            }}
            .container {{
                background: white;
                padding: 40px;
                border-radius: 12px;
                max-width: 650px;
                margin: auto;
            }}
            h1 {{ color: #1769aa; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AWS Elastic Beanstalk Deployment</h1>
            <h2>{message}</h2>
            <p>Environment: {environment}</p>
            <p>Deployment Version: 1.0</p>
            <p>Deployment Platform: AWS Elastic Beanstalk</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

application = app
