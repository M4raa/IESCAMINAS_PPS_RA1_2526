#!/bin/bash

MAC_ADDRESS=$(ip link show | awk '/ether/ {print $2; exit}')
OS_INFO=$(uname -o)
HOSTNAME=$(hostname)
CURRENT_USER=$(whoami)

echo "MAC del equipo: $MAC_ADDRESS
Sistema Operativo: $OS_INFO
Nombre del equipo: $HOSTNAME
Usuario: $CURRENT_USER"
