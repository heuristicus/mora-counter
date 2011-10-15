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
            base = args[0]
            self.sentence = filter(lambda x: x != None, [base[i:i+3].decode('utf8') if i%3 == 0 else None for i, v in enumerate(base)])
            self.check_sentence()
            self.data_init()
            print self.moraise()

    def moraise(self):
        return len(filter(lambda x: x != 's', map(self.replace, self.sentence)))
    
    def replace(self, char):
        if char in self.small:
            return 's'
        elif char in self.tsu:
            return 't'
        else:
            return char

    def data_init(self):
        # initialise lists containing symbol hex codes. contains
        # small ya,yu,yo in katakana and hiragana, as well as small
        # tsu for both.
        self.small = [u'\u3087',u'\u3083',u'\u3085',u'\u30E3',u'\u30E5',u'\u30E7']
        self.tsu = [u'\u3063',u'\u30C3']
        
        
    def check_sentence(self):
        for char in self.sentence:
            if self.jp_check(char) == False:
                print 'invalid'
                return False
        print 'input is valid'
        return True

    def jp_check(self, char):
        # For more info, see below
        # http://www.utf8-chartable.de/unicode-utf8-table.pl
        # !!!!LARGE!!!! http://www.rikai.com/library/kanjitables/kanji_codes.unicode.shtml 

        h_val = ord(char)
        # Hiragana
        if h_val >= int('3040', 16) and h_val <= int('3096',16):
            return True
        # Katakana
        elif h_val >= int('30A1',16) and h_val <= int('30FA', 16):
            return True
        # Symbols
        elif h_val >= int('3000', 16) and h_val <= int('303F',16):
            return True
        elif h_val >= int('30FB',16) and h_val <= int('30FF',16):
            return True
        elif h_val >= int('3097',16) and h_val <= int('30A0',16):
            return True
        # Kanji
        # elif h_val >= 19968 and h_val <= 40895:
        #    return True
        else:
            return False

if __name__ == '__main__':
    MoraCount()
