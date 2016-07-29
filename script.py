import time
import os

from richxerox import *
from tinydb import TinyDB, where

HOME_DIR = 'db'
# Create directory if it doesn't exist
os.system("mkdir db")
db = TinyDB('%s/db.json' % HOME_DIR)
currently_found_in_clipboard = paste(format='text')
while True:
    time.sleep(0.1) # one tenth of a second
    if paste(format='text') != currently_found_in_clipboard:
        currently_found_in_clipboard = paste(format='text')
        # When the user hits CMD+C store the clipboard in a file and take a screenshot of the screen
        created_at = time.time()
        entry = { 'content': pasteall(), 'created_at': int(created_at),}
        entry['screenshot'] = '%s/screen%s.png' % (HOME_DIR, created_at)
        os.system("screencapture %s" % entry['screenshot'])
        db.insert(entry)
