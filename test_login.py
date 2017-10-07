#author Ye Zhao

#!usr/bin.python

import pxssh

s = pxssh.pxssh()

if not s.login ('5900','cs8af8','60wnUdnR'):
    print "FAIL"
else:
    print ("SUCCESS")
    s.sendline('mkdir pa0')
    s.prompt()
    print (s.before)
    s.logout()
