# Quotes
Django app that displays random haikus created from WikiQuotes and categorized by sentiment.
# Setup
Clone the repository:
```bash
git clone https://github.com/kubczakn/Quotes.git
cd Quotes
```
Create virtual environment to install dependencies:
```bash
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```
Finally install the dependencies:
```bash
(env)$ pip install -r requirements.txt
```
# Usage
Generate a new haiku using random quotes from WikiQuote:
```bash
$ python database.py
```
Run the Django application:
```bash
$ python manage.py runserver
```
