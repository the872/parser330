# I didn't have much time to finish my testing...

#import unit test and project so we can test some stuff out
import unittest
import parser330

class TestParser(unittest.TestCase):

    def setup(self):
        self.parser = parser330.Parser()

    def test_url(self):
        test = self.parser.parse('so here is this cool url for a cool site called google. http://google.com')
        self.assertEqual(test.url, 'http://google.com/')

    def test_hastag(self):
        test = self.parser.parse('so now we have all of these cool hashtags #hashtags')
        self.assertEqual(test.hashtag, '#hastags')

    def test_users(self):
        test = self.parser.parse('great, no we only have to test a couple other things @the872')
        self.assertEqual(test.user, '@the872')

    def test_parser(self):
        test = self.parser.parse('lets #make @sure http://everythingworks.com')
        self.assertEqual(test.user, '@sure')
        self.assertEqual(test.hashtag, '#make')
        self.assertEqual(test.url, 'http://everythingworks.com')

        
