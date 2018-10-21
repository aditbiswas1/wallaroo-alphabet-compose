#!/bin/sh
export PYTHONPATH=/wallaroo-src/machida:$PYTHONPATH

cd `dirname "$0"`

machida --application-module alphabet --in 0.0.0.0:7010 \
  --out dummy_receiver:11000 --metrics wallaroo_metrics_ui:5001 --control 127.0.0.1:12500 \
  --external 127.0.0.1:5050 --cluster-initializer --data 127.0.0.1:12501 \
  --name worker-name --ponythreads=1 --ponynoblock 