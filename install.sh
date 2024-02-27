#!/usr/bin/bash
mkdir /usr/bin

cp ./minecraft-auto.service /etc/systemd/system/minecraft-auto.service

# Copy python file into /usr/bin
cp ./main.py /usr/bin/mcauto
cp ./runner.py /usr/bin/runner.py
cp ./upload.py /usr/bin/upload.py
cp config.json /usr/bin/config.json

# get the distro specific package manager
packagesNeeded='python pip systemd'
# shellcheck disable=SC2086
if [ -x "$(command -v apk)" ];       then sudo apk add --no-cache $packagesNeeded
elif [ -x "$(command -v apt-get)" ]; then sudo apt-get install "$packagesNeeded"
elif [ -x "$(command -v dnf)" ];     then sudo dnf install "$packagesNeeded"
elif [ -x "$(command -v zypper)" ];  then sudo zypper install "$packagesNeeded"
else echo "FAILED TO INSTALL PACKAGE: Package manager not found. You must manually install: $packagesNeeded">&2; fi

cd /usr/bin/ || exit

# Make file globally executable
chmod +x mcauto

# Install mcstatus from pip
pip install typer watchdog

echo "Successfully installed Minecraft Plugin Automation!"