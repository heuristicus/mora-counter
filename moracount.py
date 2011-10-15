#/usr/bin/python

import sys

class MoraCount:

    def __init__(self):
        args = sys.argv[1:]
        if not args:
            print 'Requires a sentence in hiragana, katakana or romaji'
            sys.exit(0)
        else:
            self.sentence = args[0]
        print self.sentence

if __name__ == '__main__':
    MoraCount()
