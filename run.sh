WORKDIR='/root/AppsManager'
PYTHON_PATH='venv/bin/python'
SCRIPT_PATH='__main__.py'
UNIT_NAME='apps-manager'

UNIT_TEXT="[Unit]
Description=Apps Manager
After=network.target

[Service]
Type=simple
WorkingDirectory=$WORKDIR
ExecStart=$WORKDIR/$PYTHON_PATH $SCRIPT_PATH
Restart=always

[Install]
WantedBy=multi-user.target"

python3.10 -m venv venv &&
  pipenv requirements >requirements.txt &&
  venv/bin/python -m pip install -r requirements.txt &&
  echo "$UNIT_TEXT" >"/etc/systemd/system/$UNIT_NAME.service" &&
  systemctl daemon-reload &&
  systemctl enable $UNIT_NAME &&
  systemctl start $UNIT_NAME &&
  systemctl status $UNIT_NAME
