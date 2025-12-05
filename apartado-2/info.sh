#!/bin/bash

# OS detection
OS_TYPE=$(uname -s)

# Common info by OS
HOSTNAME=$(hostname)
CURRENT_USER=$(whoami)
ARCHITECTURE=$(uname -m)

# Specific info by OS
declare MAC
declare IP

case $OS_TYPE in
    # Linux
    Linux)
        MAC=$(ip link show | grep link/ether | awk '{print $2}')
        IP=$(hostname -I | awk '{print $1}')
        ;;
    # macOS
    Darwin)
        MAC=$(ifconfig en0 | grep ether | awk '{print $2}')
        IP=$(ifconfig en0 | grep inet | awk '{print $2}')
        ;;
    # Windows (Git Bash)
    CYGWIN*|MINGW*|MSYS*)
        IP=$(powershell.exe -noprofile -command "Get-NetIPConfiguration | Where-Object { \$_.IPv4DefaultGateway -ne \$null } | Select-Object -ExpandProperty IPv4Address | Select-Object -ExpandProperty IPAddress")
        MAC=$(powershell.exe -noprofile -command "Get-NetIPConfiguration | Where-Object { \$_.IPv4DefaultGateway -ne \$null } | Select-Object -ExpandProperty NetAdapter | Select-Object -ExpandProperty MacAddress")
        ;;
    *)
        exit 1
        ;;
esac

# Show results
echo "System info"
echo "OS: $OS_TYPE"
echo "Architecture: $ARCHITECTURE"
echo "Hostname: $HOSTNAME"
echo "User: $CURRENT_USER"
echo "IP: $IP"
echo "MAC: $MAC"