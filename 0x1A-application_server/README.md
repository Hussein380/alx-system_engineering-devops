# AirBnB Clone - Web Application Server Setup

This project demonstrates how to set up a web application server using Nginx and Gunicorn to serve a Flask-based AirBnB clone application. The instructions will guide you through the development and production environments.

## Table of Contents

- [Project Description](#project-description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Description

The goal of this project is to set up a web infrastructure capable of serving a dynamic web application. The application is an AirBnB clone built with Flask, which will be served using Gunicorn and proxied through Nginx.

## Requirements

- Ubuntu 16.04 LTS
- Python 3.x
- Flask
- Gunicorn
- Nginx
- Git

## Installation

### 1. System Preparation

Update and install necessary packages:

```bash
sudo apt update
sudo apt install -y python3 python3-pip nginx git net-tools
```

### 2. Clone the Repository

Clone your AirBnB clone repository to your server:

```bash
git clone https://github.com/yourusername/AirBnB_clone_v2.git
cd AirBnB_clone_v2
```

### 3. Install Python Dependencies

Install the necessary Python packages:

```bash
pip3 install -r requirements.txt
```

## Configuration

### 1. Flask Application

Modify `web_flask/0-hello_route.py` to serve content on the `/airbnb-onepage/` route:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/airbnb-onepage/')
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### 2. Gunicorn

Install Gunicorn globally:

```bash
sudo pip3 install gunicorn
```

Run Gunicorn to serve the Flask app:

```bash
gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
```

### 3. Nginx Configuration

Create an Nginx configuration file to proxy requests to Gunicorn:

```nginx
server {
    listen 80;

    location /airbnb-onepage/ {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Save this file as `/etc/nginx/sites-available/airbnb` and create a symlink to it in the `sites-enabled` directory:

```bash
sudo ln -s /etc/nginx/sites-available/airbnb /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## Running the Application

1. Start Gunicorn in a detached mode using `tmux`:

```bash
tmux new-session -d 'gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app'
```

2. Check that Gunicorn is running:

```bash
pgrep gunicorn
```

3. Ensure Nginx is properly serving the application:

```bash
curl http://127.0.0.1/airbnb-onepage/
```

## Testing

To test that your setup works correctly, you can use `curl` from your local machine or a browser:

```bash
curl http://<your_server_ip>/airbnb-onepage/
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---
