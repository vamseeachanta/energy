## Introduction
The document describes :

This document outlines instructions to work in Linux Operating System.

## NOTES TO BE SORTED

apt-get update
 
apt-get -y install vim
 
 
??
 
SQL container. Populate it with data?
 
Login as Root:
Sudo su
 
All commands in a linux machine should work when logged in as root.
 
Ls
 
 
List process
Ps ls

General:
 
Date
 
dir
 
dir -al
dir -a
 
Environment Variables:
Printenv
 
Access an individual environment variable:
echo $MOLE_IOT 
Define an enviornment variable:
TEST_VAR='Hello World!'
MOLE_SEND_EXCEPTION_EMAILS='TRUE'
 
From <https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps> 
 
https://maker.pro/linux/tutorial/basic-linux-commands-for-beginners
 
https://www.tecmint.com/linux-commands-cheat-sheet/
 
To connect: SSH
To browse in Linux machines: use https://winscp.net/download/WinSCP-5.13.7-Setup.exe



sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git

## OS Commands

find operating system information
<pre>
    cat /etc/os-release
</pre>
example output:
<pre>
        PRETTY_NAME="Debian GNU/Linux 10 (buster)"
        NAME="Debian GNU/Linux"
        VERSION_ID="10"
        VERSION="10 (buster)"
        VERSION_CODENAME=buster
        ID=debian
        HOME_URL="https://www.debian.org/"
        SUPPORT_URL="https://www.debian.org/support"
        BUG_REPORT_URL="https://bugs.debian.org/"
</pre>

## Search

find / -type f -exec grep -H 'text-to-find-here' {} \;
 
find / -exec grep -H 'pymsssql' {} \;
grep -Ril "pymssql" /
 
From <https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux/16956844> 
 
 
From <https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux/16956844> 
 
 
find . -type f -name "*John*
 
From <https://stackoverflow.com/questions/13131048/linux-find-file-names-with-given-string> 
