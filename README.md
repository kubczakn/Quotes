# Quotes
Django app that displays random haikus created from WikiQuotes and categorized by sentiment.
# Setup
Clone the repository:
```bash
git clone https://github.com/kubczakn/Quotes.git
cd Quotes
```
Create and activate virtual environment:
```bash
$ python3 -m venv quotes-env
$ source quotes-env/bin/activate
```
Update pip and install wheel:
```bash
(quotes-env)$ pip3 install --upgrade pip
(quotes-env)$ pip3 install wheel
```
Install dependencies:
```bash
(quotes-env)$ pip install -r requirements.txt
```
# Usage
Run the Django application at http://127.0.0.1:8000/haikuApp/:
```bash
$ cd app
$ python manage.py migrate
$ python manage.py runserver
```
Populate the Django database with a new Haiku categorized by sentiment:
```bash
$ cd scripts
$ python database.py
```

