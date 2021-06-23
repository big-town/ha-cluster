#!/bin/bash
FULL="$1"
NAME="$2"
PREF=`date +%Y`/`date +%m`/`date +%d`
#CMD="pigz -1 -p40 -c ${FULL} > /mnt/backup/wals/$PREF/${NAME}.gz"
CMD="pigz -1 -p40 -c ${FULL} > /mnt/backup/wals/${NAME}.gz"
echo "$CMD"  >> /var/log/postgresql/copy_wal.log
#ssh root@10.10.10.12 "mkdir -p /mnt/backup/wals ; [ -z \"`mount | grep '/mnt/backup'`\" ] && mount.ceph 192.168.11.10,192.168.11.11,192.168.11.12:/ /mnt/backup -o name=admin,secret="
#scp -C ${FULL} root@10.10.10.12:/mnt/backup/wals &&
#rsync -az -e "ssh" ${FULL} root@10.10.10.12:/mnt/backup/wals &&
mkdir -p /mnt/backup/wals
[ -z "`mount | grep '/mnt/backup'`" ] && mount -t ceph 192.168.10.10,192.168.10.11,192.168.10.12:/ /mnt/backup -o name=admin,secret=
eval $CMD
