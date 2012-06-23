#! /usr/bin/env python2.7

from simplenote import Simplenote
import sys, time

NOTE_FORMAT = '''########################################
Created: {createdate}
Modified: {modifydate}
Tags: {tags}
Content:
{content}

'''

def check_status(status):
    if 0 != status:
        print 'An error occured while accessing Simplenote API'
        sys.exit(-1)


def main(path, user, password):
    s = Simplenote(user, password)

    notes, status = s.get_note_list()
    check_status(status)

    with open(path, 'w') as f:
        for note in notes:
            note, status = s.get_note(note['key'])
            check_status(status)

            if not note['deleted']:
                note['tags'] = ' '.join(note['tags'])
                note['createdate'] = time.strftime('%d-%m-%Y %H:%M:%S',
                    time.localtime(float(note['createdate'])))
                note['modifydate'] = time.strftime('%d-%m-%Y %H:%M:%S',
                    time.localtime(float(note['modifydate'])))
                f.write(NOTE_FORMAT.format(**note))


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print 'Please provide the path where you want your notes saved as well as the user name and dropbox password!'
