#!/usr/bin/env python3

from string import ascii_letters, digits
from itertools import chain
from random import choice
import os
import os

def create_uid(n=9):
   '''Génère une chaîne de caractères alétoires de longueur n
   en évitant 0, O, I, l pour être sympa.'''

   chrs = [ c for c in chain(ascii_letters,digits)
                        if c not in '0OIl'  ]
   return ''.join( ( choice(chrs) for i in range(n) ) )

def save_doc_as_file(uid=None,code=None,language=None):
    '''Crée/Enregistre le document sous la forme d'un fichier
    data/uid. Return the file name.
    '''
    if uid is None:
        uid = create_uid()+'.py'
        code = '# Write your code here...'
    else:
        ext = os.path.splitext('data/{}'.format(uid))
        if ext != language:
            new = uid.replace(ext[1], language)
            old = uid
            uid = new
            os.remove('data/{}'.format(old))

    with open('data/{}'.format(uid),'w') as fd:
        fd.write(code)

    return uid

def read_doc_as_file(uid):
    '''Lit le document data/uid'''
    try:
        with open('data/{}'.format(uid)) as fd:
            code = fd.read()
        return code
    except FileNotFoundError:
        return None

def get_last_entries_from_files(n=10,nlines=10):
    entries = os.scandir('data')
    d = []
    entries = sorted(list(entries),
                     key=(lambda e: e.stat().st_mtime),
                     reverse=True) 
    for i,e in enumerate(entries):
        if i >= n:
            break
        if e.name.startswith('.'):
            continue
        with open('data/{}'.format(e.name)) as fd:
            code = ''.join(( fd.readline() for i in range(nlines) ))
            if fd.readline():
                code += '\n...'
        d.append({ 'uid':e.name, 'code':code })
    return d

