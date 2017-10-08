#author Ye Zhao

#!usr/bin.python

from pexpect import pxssh

s = pxssh.pxssh()

if not s.login ('cs8af46@ieng6.ucsd.edu','cs8af15','60wnUndR'):
    print ("FAIL")
else:
    print ("SUCCESS")
    s.sendline('mkdir pa0')
    s.prompt()
    print (s.before)
    s.logout()
