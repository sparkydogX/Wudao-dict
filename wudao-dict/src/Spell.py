import os
import json
import random
from pprint import pprint
import sys


class DictationClass():
    # UNDERLINEPATTERN = '\033[4m%s\033[0m'
    UNDERLINEPATTERN = '    \033[6;30;42m%s\033[0m'
    NOTE_NAME = './usr/notebook.txt'
    MISTAKE_COLLECTION = './usr/mistake_collection.json'

    def __init__(self):

        if not os.path.exists(self.MISTAKE_COLLECTION):
            with open(self.MISTAKE_COLLECTION, 'w+') as f:
                tmp_dict = {}
                json.dump(tmp_dict, f)

        f = open(self.NOTE_NAME, 'r')
        lines = f.readlines()
        self.notebook = {}
        self.ischange = False
        for line in lines:
            tmplist = line.split()
            k = tmplist[0]
            tl = [x + ' ' for x in tmplist[1:]]
            v = ''.join(tl)
            self.notebook[k] = v
        self.wrongcollection = json.load(open(self.MISTAKE_COLLECTION))
        self.indexList = list(range(len(self.notebook)))
        self.keyList = list(self.notebook.keys())
        random.shuffle(self.indexList)
        self.curindex = -1
        self.auto = True
        self.commandlist = ['n', 'r', 'h', 'd', 'q', 'l', 'i', '']
        print('Welcome to dictation.')
        print('There are {0} words in notebook.'.format(len(self.notebook)))

    def run(self):
        while True:
            rows, columns = os.popen('stty size', 'r').read().split()
            print('-' * int(columns))
            print('\x1b[6;30;42m' +
                  'n' + '\x1b[0m' + 'ext' +
                  self.UNDERLINEPATTERN % 'r' + 'etry' +
                  self.UNDERLINEPATTERN % 'h' + 'elp' +
                  self.UNDERLINEPATTERN % 'l' + 'ook_up' +
                  self.UNDERLINEPATTERN % 'i' + 'nfo' +
                  self.UNDERLINEPATTERN % 'd' + 'elete' +
                  self.UNDERLINEPATTERN % 'q' + 'uit' + ' :'
                  , end='')
            # print(':', end=' ')
            cmd = input().strip()

            if not cmd in self.commandlist:
                print('Command Not Supported.Please Input Valid command.')
            elif cmd == 'q':
                self.quitspell()
            elif cmd == 'h':
                print('Nothing meaningful here.')
            elif cmd == 'n' or cmd == '':
                IsAnswerCorrect = False
                self.curindex += 1
                if self.curindex >= len(self.notebook):
                    print('All Done.')
                    self.quitspell()
                for _ in range(2):
                    IsAnswerCorrect = self.spell()
                    if IsAnswerCorrect:
                        break
                if not IsAnswerCorrect:
                    self.lookup()

            elif cmd == 'r':
                self.retry()
            elif cmd == 'l':
                self.lookup()
            elif cmd == 'd':
                self.deleteEntry()
            elif cmd == 'p':
                pprint(self.notebook)
            elif cmd == 'i':
                self.info()

    def spell(self):
        k = self.keyList[self.indexList[self.curindex]]
        try:
            v = self.notebook[k]
        except Exception:
            print(k + ' does not exist in notebook now.')
            return
        print(v)
        print(':', end='')
        answer = input().strip()
        if answer == k:
            print('Correct.')
            return True
        else:
            print('Wrong. Please Try Anagin.')
            self.wrongcollection[k] = self.wrongcollection.get(k, 0) + 1
            return False

    def retry(self):
        self.curindex = max(self.curindex, 0)
        self.spell()

    def lookup(self):
        self.curindex = max(self.curindex, 0)
        k = self.keyList[self.indexList[self.curindex]]
        os.system('wd ' + k)

    def info(self):
        sorted_by_value = sorted(self.wrongcollection.items(), key=lambda kv: kv[1], reverse=True)
        print('错误统计:')
        displen = min(50, len(sorted_by_value))
        for elem in sorted_by_value[:displen]:
            print('{0:<20} {1:>3}'.format(elem[0], elem[1]))

    def deleteEntry(self):
        self.curindex = max(self.curindex, 0)
        k = self.keyList[self.indexList[self.curindex]]
        self.notebook.pop(k)
        self.ischange = True
        print(k + ' is deleted from notebook now.')

    def quitspell(self):
        if self.ischange:
            print('Saving changes...')
            with open(self.NOTE_NAME, 'w') as f:
                for k, v in self.notebook.items():
                    spaces = ' ' * (20 - len(k))
                    f.write(k + spaces + ' ' + v + '\n')
        with open(self.MISTAKE_COLLECTION, 'w') as f:
            json.dump(self.wrongcollection, f)
        print('See You.')
        exit(0)


if __name__ == '__main__':
    spell = DictationClass()
    spell.run()
