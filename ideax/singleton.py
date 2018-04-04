from wordfilter import Wordfilter
import os
import json

class Profanity_Check:
    __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, 'badwords.json')) as f:
        blacklist = json.loads(f.read())

    wordfilter = Wordfilter()
    wordfilter.add_words(blacklist)

    @classmethod
    def wordcheck(cls, *args, **kwargs):
        return cls.wordfilter
