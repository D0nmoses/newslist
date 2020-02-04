import unittest
from app.models import NewsArticle
import datetime

class NewsArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsArticle class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = NewsArticle(1,"Don Moses","Coronavirus Scare","Panic as patient hospitalized in Coast with fears of Coronavirus","https://stuff.com","https://stuff_image.com",datetime.date())

    def test_instance(self):
        '''
        method asserts existence of an instance
        :return:
        '''
        self.assertTrue(isinstance(self.new_article,NewsArticle))