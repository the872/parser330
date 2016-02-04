# I didn't have much time to finish my testing...

#import unit test and project so we can test some stuff out
import unittest
import parser330

class TestParser(unittest.TestCase):

    def setup(self):
        self.parser = parser330.Parser()

    def test_url(self):
        test0 = self.parser.parse('so here is this cool url for a cool site called google. http://google.com')
        self.assertEqual(test0.url, 'http://google.com')
        test1 = self.parser.parse('here is as newhttp:jknoot .com #@ http://google.com for this')
        self.assertEqual(test1.url, 'http://google.com')
        test2 = self.parser.parse('lets do one with no link to see if its going well')
        self.assertEqual(test2.url, '')

    def test_hastag(self):
        test0 = self.parser.parse('so now we have all of these cool hashtags #hashtags')
        self.assertEqual(test0.hashtag, '#hastags')
        test1 = self.parser.parse('google.#hastag son')
        self.assertEqual(test1.hashtag, 'hashtag')
        test2 = self.parser.parse('lets see what it does when there are no hashtags')
        self.assrtEqual(test2.hashtag, '')

    def test_users(self):
        test0 = self.parser.parse('great, no we only have to test a couple other things @the872')
        self.assertEqual(test0.user, '@the872')
        test1 = self.parser.parse('http:notaurl@the872')
        self.assertEqual(test1.user, '@the872')
        test2 = self.parser.parse('no users to find here')
        self.assertEqual(test2.user, '')

    def test_parser(self):
        test0 = self.parser.parse('lets #make @sure http://everythingworks.com')
        self.assertEqual(test0.user, '@sure')
        self.assertEqual(test0.hashtag, '#make')
        self.assertEqual(test0.url, 'http://everythingworks.com')
        test1 = self.parser.parse('what #if @things are missing')
        self.assertEqual(test1.user, '@things')
        self.assertEqual(test1.hashtag, '#if')
        self.assertEqual(test1.url, '')
        test2 = self.parser.parse('nothing to parse here')
        self.assertEqual(test2.user, '')
        self.assertEqual(test2.hashtag, '')
        self.assertEqual(test2.url, '')

        
