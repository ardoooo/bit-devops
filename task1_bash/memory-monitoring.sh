#!/bin/bash

PIDFILE="/tmp/memory-monitoring.pid"

start() {
  if [ -e $PIDFILE ]; then
    echo "Process is already running"
  else
    timestamp=$(date +%Y.%m.%d_%H.%M.%S)
    log_file="/tmp/memory-monitoring-logs_${timestamp}.csv"

    echo "timestamp_s,total,used,free" > $log_file
    while true; do
      timestamp=$(date +%Y.%m.%d_%H.%M.%S)
      memory_info=$(free | grep 'Mem')
      total=$(echo $memory_info | awk '{ print $2}')
      used=$(echo $memory_info | awk '{ print $3}')
      free=$(echo $memory_info | awk '{ print $4}')
      echo "$timestamp,$total,$used,$free" >> $log_file

      sleep 600
    done &
    echo $! > $PIDFILE
  fi
}

stop() {
  if [ ! -e $PIDFILE ]; then
    echo "Process is not running"
  else
    kill $(cat $PIDFILE)
    rm $PIDFILE
  fi
}

status() {
  if [ -e $PIDFILE ]; then
    echo "Running"
  else
    echo "Not running"
  fi
}

case "$1" in
  START)
    start
    ;;
  STOP)
    stop
    ;;
  STATUS)
    status
    ;;
  *)
    echo "Invalid argument"
esac

exit 0