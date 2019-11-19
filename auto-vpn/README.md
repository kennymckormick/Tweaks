# README

- to use this script, merge these files to your vpn config folder:
  - your vpn config folder should have:
    - xxx.ovpn
    - ca.crt
    - ta.key
- then fill in configs in reconnect.py
- then start a tmux session, change to user root, and execute './auto-ovpn.sh', you will have your vpn always running 



PS: to make your SSH session always alive, you also need to change 'ServerAliveInterval' in '~/.ssh/config' to a large number (like > 240, etc.)
