from flask import Flask, session, request

app = Flask(__name__)

@app.route('/')
def main():
  return 'Hello world'

@app.route('/getSessionVar', methods=['GET', 'POST'])
def getSessionVariable():
  if 'GET' == request.method:
    session['sessionVar'] = 'hello'
  elif 'POST' == request.method:
    session['sessionVar'] = 'hi'
  else:
    session['sessionVar'] = 'error'

  return 'ok'


@app.route('/changeSessionVar')
def changeSessionVariable():
  if session['existingSessionVar'] != 'hello':
    raise Exception('unexpected session value of existingSessionVar!')

  session['existingSessionVar'] = 'hello world'
  return 'ok'


if __name__ == '__main__':
  app.run()

app.secret_key = 'my-seCret_KEy'