#!/bin/sh
export PYTHONPATH=/wallaroo-src/machida:$PYTHONPATH

cd `dirname "$0"`

data_receiver --ponythreads=1 --ponynoblock \
  --listen 0.0.0.0:11000