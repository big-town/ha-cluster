
#!/bin/bash
FULL="$1"
NAME="$2"
CMD="pigz -1 -p40 -c -d /mnt/backup/wals/${NAME}.gz > ${FULL}"
echo "$CMD"  >> /var/log/postgresql/restore_wal.log
#ssh root@10.10.10.12 "mkdir -p /mnt/backup/wals ; [ -z \"`mount | grep '/mnt/backup'`\" ] && mount.ceph 192.168.11.10,192.168.11.11,192.168.11.12:/ /mnt/backup -o name=admin,secret="
#scp -C ${FULL} root@10.10.10.12:/mnt/backup/wals &&
#rsync -az -e "ssh" ${FULL} root@10.10.10.12:/mnt/backup/wals &&
#mkdir -p /mnt/backup/wals
[ -z "`mount | grep '/mnt/backup'`" ] && mount -t ceph 192.168.10.10,192.168.10.11,192.168.10.12:/ /mnt/backup -o name=admin,secret=
eval $CMD
#sh root@10.10.10.12 "pigz -1 -p40 /mnt/backup/wals/${NAME} &"
#/usr/local/bin/pgbackrest --stanza=main archive-push $FULL