import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(1,"Washington Post", "Leading news outlet", "http://stuff.com", "business", "US", "en")

    def test_instance(self):
        '''
        method asserts existence of an instance
        :return:
        '''
        self.assertTrue(isinstance(self.new_source,Source))