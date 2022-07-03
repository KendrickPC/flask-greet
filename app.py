from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
  """
  Returns a simple "welcome" greeting.
  """
  html = "welcome"
  return html

@app.route('/welcome/home')
def say_welcome_home():
  """
  Returns a simple "welcome home" greeting.
  """
  html = "welcome home"
  return html

@app.route('/welcome/back')
def say_welcome_back():
  """
  Returns a simple "welcome back" greeting.
  """
  html = "welcome back"
  return html

