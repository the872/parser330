# import regex libraries so we can get to business
import re

class Parser(object):


    def __init__(self):

        # The following regex was formally taken from https://github.com/edburnett/twitter-text-python
        # It is the official twitter regex project in Python
        # I took what I needed and made some formatting changes so it better fit my project

        # General
        self.AT_SIGNS = r'[@\uff20]'
        self.UTF_CHARS = r'a-z0-9_\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff'
        self.LIST_END_CHARS = r'([a-z0-9_]{1,20})(/[a-z][a-z0-9\x80-\xFF-]{0,79})?'

        # Users
        self.USERNAME_REGEX = re.compile(r'\B' + self.AT_SIGNS + self.LIST_END_CHARS, re.IGNORECASE)

        # Hashtags
        self.HASHTAG_EXP = r'(^|[^0-9A-Z&/]+)(#|\uff03)([0-9A-Z_]*[A-Z_]+[%s]*)' % self.UTF_CHARS
        self.HASHTAG_REGEX = re.compile(self.HASHTAG_EXP, re.IGNORECASE)


        # URLs
        self.PRE_CHARS = r'(?:[^/"\':!=]|^|\:)'
        self.DOMAIN_CHARS = r'([\.-]|[^\s_\!\.\/])+\.[a-z]{2,}(?::[0-9]+)?'
        self.PATH_CHARS = r'(?:[\.,]?[%s!\*\'\(\);:=\+\$/%s#\[\]\-_,~@])' % (self.UTF_CHARS, '%')
        self.QUERY_CHARS = r'[a-z0-9!\*\'\(\);:&=\+\$/%#\[\]\-_\.,~]'

        # Valid end-of-path chracters (so /foo. does not gobble the period).
        # 1. Allow ) for Wikipedia URLs.
        # 2. Allow =&# for empty URL parameters and other URL-join artifacts
        self.PATH_ENDING_CHARS = r'[%s\)=#/]' % self.UTF_CHARS
        self.QUERY_ENDING_CHARS = '[a-z0-9_&=#]'

        self.URL_REGEX = re.compile('((%s)((https?://|www\\.)(%s)(\/(%s*%s)?)?(\?%s*%s)?))'
                                    % (self.PRE_CHARS, self.DOMAIN_CHARS, self.PATH_CHARS,
                                        self.PATH_ENDING_CHARS, self.QUERY_CHARS, self.QUERY_ENDING_CHARS),
                                    re.IGNORECASE)

    def parse(self, tweet):
        matches = {
            'tweet': self.tweet,
            'user': self.get_users(tweet),
            'hashtag': self.get_hashtag(tweet),
            'url': self.get_url(tweet)
        }
        return matches 

    def get_users(self, tweet):
        matches = re.findall(self.USERNAME_REGEX, tweet)
        return matches

    def get_hashtag(self, tweet):
        matches = re.findall(self.HASHTAG_REGEX, tweet)
        return matches

    def get_url(self, tweet):
        matches = re.findall(self.URL_REGEX, tweet)
        return matches
