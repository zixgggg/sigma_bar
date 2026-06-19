#!/usr/bin/bash
git clone https://github.com/zixgggg/sigmabar.git
cd sigmabar/
chmod +x sigmabar
mkdir -p $HOME/.local/bin
cp sigmabar $HOME/.local/bin/sigmabar
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    # 檢查 ~/.bashrc 裡是不是早就已經有這行字了
    if ! grep -q '.local/bin' "$HOME/.bashrc" 2>/dev/null; then
		echo export PATH="$HOME/.local/bin:$PATH" >> "$HOME/.bashrc"
	fi
fi
mkdir -p $HOME/.config/sigmabar/
cp config.ini $HOME/.config/sigmabar/

