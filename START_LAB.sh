#!/bin/bash

SRC_DIR=${0%/*}

DEST_DIR=/tmp/initial_${DIR}

[ $SRC_DIR = "." ] &&
    DEST_DIR=/tmp/initial_docker-examples

[ ! -d /tmp/initial_${DIR} ] &&
    rsync -a ${SRC_DIR} ${DEST_DIR}

find $SRC_DIR/ -iname 'docker-compose.yml*' -exec rm {} \;
find $SRC_DIR/ -iname 'Dockerfile*'         -exec rm {} \;
find $SRC_DIR/ -iname '*build*.sh'          -exec rm {} \;




