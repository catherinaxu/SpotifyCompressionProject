#!/bin/bash
brew -v &> /dev/null
if [ $? -ne 0 ]; then
    echo "Homebrew not found, installing Homebrew"
    bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
fi

brew install python

python3 -m venv python/venv
source python/venv/bin/activate

pip install --upgrade pip
pip install spotipy