#!/bin/sh

set -e

clouderp_CONFIGURATION_DIR=/etc/clouderp
clouderp_CONFIGURATION_FILE=$clouderp_CONFIGURATION_DIR/gce-server.conf
clouderp_DATA_DIR=/var/lib/clouderp
clouderp_GROUP="clouderp"
clouderp_LOG_DIR=/var/log/clouderp
clouderp_USER="clouderp"

if ! getent passwd | grep -q "^clouderp:"; then
    groupadd $clouderp_GROUP
    adduser --system --no-create-home $clouderp_USER -g $clouderp_GROUP
fi
# Register "$clouderp_USER" as a postgres user with "Create DB" role attribute
su - postgres -c "createuser -d -R -S $clouderp_USER" 2> /dev/null || true
# Configuration file
mkdir -p $clouderp_CONFIGURATION_DIR
# can't copy debian config-file as addons_path is not the same
if [ ! -f $clouderp_CONFIGURATION_FILE ]
then
    echo "[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = $clouderp_USER
db_password = False
addons_path = /usr/lib/python2.7/site-packages/gce/addons
" > $clouderp_CONFIGURATION_FILE
    chown $clouderp_USER:$clouderp_GROUP $clouderp_CONFIGURATION_FILE
    chmod 0640 $clouderp_CONFIGURATION_FILE
fi
# Log
mkdir -p $clouderp_LOG_DIR
chown $clouderp_USER:$clouderp_GROUP $clouderp_LOG_DIR
chmod 0750 $clouderp_LOG_DIR
# Data dir
mkdir -p $clouderp_DATA_DIR
chown $clouderp_USER:$clouderp_GROUP $clouderp_DATA_DIR

INIT_FILE=/lib/systemd/system/clouderp.service
touch $INIT_FILE
chmod 0700 $INIT_FILE
cat << 'EOF' > $INIT_FILE
[Unit]
Description=clouderp Open Source ERP and CRM
After=network.target

[Service]
Type=simple
User=clouderp
Group=clouderp
ExecStart=/usr/bin/clouderp.py --config=/etc/clouderp/gce-server.conf

[Install]
WantedBy=multi-user.target
EOF
easy_install pyPdf vatnumber pydot psycogreen suds ofxparse
