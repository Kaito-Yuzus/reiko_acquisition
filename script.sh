#!/system/bin/sh
set -x
tar -czvf /storage/emulated/0/target/extraction.tar.gz /data --transform 's|^|Dump/|S'