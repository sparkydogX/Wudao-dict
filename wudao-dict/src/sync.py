import os
from bypy import ByPy
from shutil import copyfile
SYNC_DIR = './usr/sync'
USR_DIR = './usr'

def Sync_Up():
    bp = ByPy()
    bp.mkdir('wudao-dict')
    if not os.path.exists(SYNC_DIR):
        os.makedirs(SYNC_DIR)
    sync_file_list=['mistake_collection.json','notebook.txt','usr_word.json']
    for f in sync_file_list:
        copyfile(os.path.join(USR_DIR,f),os.path.join(SYNC_DIR,f))
    bp.upload(localpath=SYNC_DIR,remotepath='wudao-dict')
    print('Sync: Upload complete.')

def Sync_Down():
    bp = ByPy()
    if not os.path.exists(SYNC_DIR):
        os.makedirs(SYNC_DIR)
    bp.downdir(remotepath='wudao-dict',localpath=SYNC_DIR)
    sync_file_list=['mistake_collection.json','notebook.txt','usr_word.json']
    for f in sync_file_list:
        copyfile(os.path.join(SYNC_DIR,f),os.path.join(USR_DIR,f))
    print('Sync: Download Complete.')

if __name__ == '__main__':
    Sync_Down()