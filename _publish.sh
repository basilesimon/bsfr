#!/bin/sh
# -----------------------------------------------------------
# commit-vps.sh
# -----------------------------------------------------------

localhugo="${HOME}/github/bsfr"
remotewebroot="/var/www/basilesimon.fr"
instancehost="51.159.139.203"
sshuser="b"
sshport="22"
sshidentity="${HOME}/.ssh/id_rsa"


cd $localhugo
/usr/local/bin/hugo

echo "rsync to SSH host $instancehost ..."
rsync -vrhp -e "ssh -p $sshport -i $sshidentity" --exclude ".*" --delete-after \
  --chmod=Du=rwx,Dg=rx,Do=rx,Fu=rw,Fg=r,Fo=r \
  $localhugo/public/ $sshuser@$instancehost:$remotewebroot

echo "SSH connection closed. Done."
