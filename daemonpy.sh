#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Replace 'path_to_your_python_app' with the actual path to your Python application script.
APP_PATH="/home/optic4l/Desktop/TT/Scripts/process_script.py"
PID_FILE="/var/run/process_script.pid"

start() {
    if [ -f $PID_FILE ]; then
        echo "The service is already running."
    else
        nohup python3 $APP_PATH &> /dev/null &
        echo $! > $PID_FILE
        chmod 644 $PID_FILE
        echo "Service started."
    fi
}

stop() {
    if [ -f $PID_FILE ]; then
        kill $(cat $PID_FILE)
        rm -f $PID_FILE
        echo "Service stopped."
    else
        echo "The service is not running."
    fi
}

restart() {
    stop
    start
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
esac