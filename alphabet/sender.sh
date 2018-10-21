#!/bin/sh
export PYTHONPATH=/wallaroo-src/machida:$PYTHONPATH

cd `dirname "$0"`

sender --host wallaroo_primary_worker:7010 --file votes.msg \
  --batch-size 50 --interval 10_000_000 --messages 1000000 --binary \
  --msg-size 9 --repeat --ponythreads=1 --ponynoblock --no-write