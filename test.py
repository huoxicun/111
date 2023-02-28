import os
import git


def update(path):
    # com= "svn update %s" % (path)
    com = 'git pull %s' % (path)
    print(com)
    myrequest=os.system(com)
    if myrequest != 0:
    #    com= "svn cleanup %s" % (path)
        com='git clean '
        print(com)
        os.system(com)
        # com= "svn update %s" % (path)
        com= 'git pull %s' % (path)
        myrequest=os.system(com)
        print(com)
    return myrequest

def push():
    com = 'git add . && git commit -m "test"'
    print(com)
    os.system(com)

push()