#!/bin/bash

SRC_DIR=${0%/*}

DEST_DIR=/tmp/initial_${DIR}


[ ! -d /tmp/initial_${DIR} ] &&
    rsync -a ${SRC_DIR} ${DEST_DIR}

find $DIR/ -name 'docker-compose.yml*' -exec rm {} \;
find $DIR/ -name 'Dockerfile*'         -exec rm {} \;




