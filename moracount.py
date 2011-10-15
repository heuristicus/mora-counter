#/usr/bin/python

import sys

class MoraCount:

    def __init__(self):
        args = sys.argv[1:]
        if not args:
            print 'Requires an input in hiragana or katakana'
            sys.exit(0)
        else:
            # Get the characters back into the form \xx\yy\zz
            self.sentence = filter(lambda x: x != None, [s[i:i+3] if i%3 == 0 else None for i, v in enumerate(s)])
            self.check_sentence()
            self.data_init()

    def data_init(self):
        print 'not ready'

    def check_sentence(self):
        for char in self.sentence:
            if self.jp_check(char) == False:
                print 'invalid'
                return False
        print 'input is valid'
        return True

    def jp_check(self, char):
        h_val = ord(char)
        # Katakana
        if h_val >= 12352 and h_val <= 12447:
            return True
        # Hiragana
        elif h_val >= 12448 and h_val <= 12543:
            return True
        # Kanji
        # elif h_val >= 19968 and h_val <= 40895:
        #    return True
        else:
            return False

if __name__ == '__main__':
    MoraCount()
