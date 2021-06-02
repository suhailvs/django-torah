from django.test import TestCase, Client

from django.urls import reverse
from django.template import Template, Context


from torah.models import Word, Line
from torah import scripts


class DataTest(TestCase):

    def setUp(self):
        self.client = Client()
        # helper = scripts.LoadData()
        # helper.load_words()

    def test_data_loaded_correctly(self):
        # get genesis, line 3:21
        line = Line.objects.get(title='genesis',chapter_no=2,line_no=20)
        print(line.name)
        print([w.name for w in line.word_set.all()])
        # words missing 14 , 15