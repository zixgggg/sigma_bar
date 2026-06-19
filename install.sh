#!/usr/bin/bash
git clone https://github.com/zixgggg/sigmabar.git
cd sigmabar/
chmod +x sigmabar
mkdir -p $HOME/.local/bin
cp sigmabar $HOME/.local/bin/sigmabar
mkdir -p $HOME/.config/sigmabar/
cp config.ini $HOME/.config/sigmabar/

