import unittest
import requests

class Server(unittest.TestCase):
	def setUp(self):
		self.browser = requests.get('http://127.0.0.1:8000/')
	
	def test_status(self):
		self.assertEqual(True, self.browser.ok)


if __name__ == "__main__":
	unittest.main()
	print('ok')	
