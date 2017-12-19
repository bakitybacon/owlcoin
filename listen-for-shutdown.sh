#! /bin/sh

### BEGIN INIT INFO
# Provides:		listen-for-shutdown.py
# Required-Start:	$remote_fs $syslog
# Required-Stop:	$remote_fs $syslog
# Default-Start:	2 3 4 5
# Default-Stop:		0 1 6
### END INIT INFO

case "$1" in
  start)
   echo "Starting listen-for-shutdown.py"
   /home/pi/adafruitdisplay.py "Welcome to{Owlcoin!"
   /usr/local/bin/listen-for-shutdown.py &
   sleep 5
   runuser -l pi -c "/home/pi/update_display_asynch.sh &"
   ;;

  stop)
   echo "Stopping listen-for-shutdown.py"
   pkill -f /usr/local/bin/listen-for-shutdown.py
   ;;

  *)
   echo "Usage: /etc/init.d/listen-for-shutdown.sh {start|stop}"
   exit 1
   ;;
esac

exit 0
