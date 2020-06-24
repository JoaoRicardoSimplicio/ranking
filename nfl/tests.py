from django.test import TestCase
from django.urls import reverse

class NflApi(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('all_nfl_teams'))


    def test_nfl_list_teams(self):
        self.assertEqual(self.response.status_code, 200)
        
        
    