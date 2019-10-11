#!/bin/bash

application_name="KITT Talk"

echo "#################################################"
echo -e "#\t\t$application_name\t\t\t#"
echo -e "#\tThank you for using $application_name!\t\t#"
echo -e "#\tAuthor: Dominik Mack \t\t\t#"
echo -e "#\tContact: dominik.mack@icloud.com\t#"
echo -e "#\tGithub: Severon96\t\t\t#"
echo "#################################################"
echo
echo "If the Script fails because of missing Admin privileges, run it again with the sudo-Command."
echo

command -v python >/dev/null 2>&1 || {
    echo "Python is required for $application_name."
    echo "Please install it for the application to work."
    exit
}

echo "Great, Python is installed. Now we can proceed."

command -v pip >/dev/null 2>&1 || {
    echo "Pip is required for $application_name."
    echo "Please install it for the application to work."
    exit
}

echo "Great, Pip is installed. Now we can proceed."

pip install mutagen
pip install python-vlc

