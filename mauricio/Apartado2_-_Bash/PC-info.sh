#!/bin/bash

## funciones
get_mac_address() {
    ifconfig -a | grep -i ether | awk '{print $2}' | head -n 1
}

get_ip_address() {
    ip addr show | grep 'inet ' | awk '{print $2}' | head -n 1 | cut -d'/' -f1
}

get_os() {
    if grep -q "Microsoft" /proc/version; then
        echo "Windows (WSL)"
    else
        echo "Linux"
    fi
}

get_kernel_version() {
    uname -r
}

get_hostname_and_user() {
    local hostname=$(hostname)
    local user=$(whoami)
    echo "$hostname - $user"
}

## variables
mac_address=$(get_mac_address)
ip_address=$(get_ip_address)
os=$(get_os)
kernel_version=$(get_kernel_version)
hostname_and_user=$(get_hostname_and_user)

## out
echo "================== -- PC Info Fetch -- ==================\n nombre del equipo y usuario: $hostname_and_user \n dirección MAC: $mac_address \n sistema Operativo: $os, $kernel_version \n========================================================="