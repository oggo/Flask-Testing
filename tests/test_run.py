'''Created on 12.05.2017
@author: oggo'''

import flask
import unittest
import flask_testing
from myapp.run import app


class TestMyApp(flask_testing.TestCase):

  def create_app(self):
    return app

  def testOne(self):
    response = self.client.get('/', content_type='html/text')
    self.assertEqual(response.status_code, 200)

  def testSession1(self):
    with app.test_client() as lTestClient:
      lResp= lTestClient.get('/getSessionVar')
      self.assertEqual(lResp.status_code, 200)
      self.assertEqual(flask.session['sessionVar'], 'hello')

  def testSession2(self):
    with app.test_client() as lTestClient:
      lResp= lTestClient.post('/getSessionVar')
      self.assertEqual(lResp.status_code, 200)
      self.assertEqual(flask.session['sessionVar'], 'hi')

  def testSession3(self):
    with app.test_client() as lTestClient:
      #keep the session
      with lTestClient.session_transaction() as lSess:
        lSess['existingSessionVar'] = 'hello'

      lResp = lTestClient.get('/changeSessionVar')
      self.assertEqual(lResp.status_code, 200)
      self.assertEqual(flask.session['existingSessionVar'], 'hello world')


if __name__ == "__main__":
  #import sys;sys.argv = ['', 'Test.testName']
  unittest.main()