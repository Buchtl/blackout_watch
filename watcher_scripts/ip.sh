#!/bin/bash

getIp()
{
  echo $(ip -4 -br a | egrep -o '192.{3}[0-9].[0-9]{1,3}.[0-9]{1,3}')
}


IP=""

while [ -z "$IP" ]
do
    IP=$(getIp)
done

echo "ip = $IP"