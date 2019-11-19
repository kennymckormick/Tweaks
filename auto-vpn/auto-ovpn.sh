#!/bin/bash
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin

### Thanks Xream's Work XD

# if you don't have several vpn servers to select, you can comment following line 
# and use your openvpn config file name to replace "${host}.ovpn" in while loop.


function getStatus () {
	ifconfig | grep $1 && return 1
	return 0
}

while [[ 1 ]]; do
	getStatus tun0
	if [[ $? == 0 ]]; then
		echo "openvpn is not connected!"
		echo "Reconnecting!"
                #Replace your_sudo_password to your real user sudo password.
		python2 reconnect.py & 
		sleep 60
	fi
	sleep 60
done
