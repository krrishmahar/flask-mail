# Flask Mail Demo

A simple Flask application demonstrating how to send emails using Flask-Mail and the Sendinblue SMTP server.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Side Chick](#side-chick)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [LICENSE](#license)

## Introduction

This project showcases a minimal setup for sending emails in a Flask web application using the Flask-Mail extension and Sendinblue as the SMTP server.

## Side Chick
**configure your STMP-server to get necessary key-value**
- Login to [https://www.brevo.com/](Brevo.com)
- Go to Dashboard, configure Senders or Domains(if any)
- In Dashboard, copy {Login, Master Password} 

## Project Structure
``` sh
    flask-mail-demo/
    │
    ├── app/
    │ ├── init.py
    │ ├── routes.py
    │
    ├── config.py
    ├── .env
    ├── .flaskenv
    ├── requirements.txt
    ├── LICENSE
    └── README.md
```

## Requirements

- Python 3.6+
- Flask
- Flask-Mail
- python-dotenv

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/flask-mail-demo.git
   cd flask-mail-demo
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. **Environment Variables: Create a .env file in the root directory with the following content Or Modify mine:**
    ```sh
    MAIL_SERVER=smtp-relay.sendinblue.com
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=          #write {Login} in SMTP & API in brevo dashboard
    MAIL_PASSWORD=          #write {Master Password} in SMTP & API in brevo dashboard
    MAIL_DEFAULT_SENDER=    #write email used to login in brevo or your own domain
    ```
 
2. **Flask Environment Variables: Create a .flaskenv file in the root directory with the following content Or Modify mine:**
    ```sh
    FLASK_APP=__init__.py
    FLASK_ENV=development
    ```

## Running the Application

1. **Run the application:**
    ```sh
    flask run
    ```

2. **Access the application:**
    
Navigate to http://127.0.0.1:5000/ in your web browser. If the email is sent successfully, you will receive a JSON response confirming the message was sent.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. Contributions are welcome!

Hit the ⭐ button if you found this useful.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy Coding!
