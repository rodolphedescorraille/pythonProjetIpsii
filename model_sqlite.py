#!/usr/bin/env python3

from string import ascii_letters, digits
from itertools import chain
from random import choice
import os
import os, sys
import sqlite3

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
        uid = create_uid()
        code = '# Write your code here...'
        conn = sqlite3.connect('myDB.db')
        cur = conn.cursor()
        req = "INSERT INTO code VALUES ('"+uid+"', '"+code+"', '.py')"
        cur.execute(req)
        conn.commit()
        conn.close()
    else:
        conn = sqlite3.connect('myDB.db')
        cur = conn.cursor()
        req = "UPDATE CODE SET code = '"+code+"', language = '"+language+"' WHERE uid = '"+uid+"'"
        cur.execute(req)
        conn.commit()
        conn.close()

    return uid

def read_doc_as_file(uid):
    '''Lit le document data/uid'''
    try:
        conn = sqlite3.connect('myDB.db')
        cur = conn.cursor()
        req = "SELECT * FROM code WHERE uid = '"+uid+"'"
        cur.execute(req)
        res = cur.fetchone()
        conn.commit()
        conn.close()
        return res
    except FileNotFoundError:
        return None

def get_last_entries_from_files(n=10,nlines=10):
    conn = sqlite3.connect('myDB.db')
    cur = conn.cursor()
    req = "SELECT * FROM code"
    cur.execute(req)
    res = cur.fetchmany(10)
    conn.commit()
    conn.close()
    d = []
    for e in res:
        d.append({ 'uid':e[0], 'code':e[1], 'language':e[2] })
    return d

