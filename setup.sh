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

command -v python3 >/dev/null 2>&1 || {
    echo "Python3 is required for $application_name."
    echo "Please install Python3 to continue the installation."
    exit
}

echo "Great, Python3 is installed. Now we can proceed."

command -v pip >/dev/null 2>&1 || {
    echo "Pip is required for $application_name."
    echo "Starting Pip-Installation..."
    curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
    sudo python get-pip.py
}

echo "Great, Pip is installed. Now we can proceed."

pip3 install mutagen
pip3 install python-vlc

