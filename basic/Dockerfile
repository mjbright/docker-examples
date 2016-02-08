#
# Dockerfile to demonstrate the simplest build
#

FROM python

MAINTAINER "Docker Build Lab" <dockerlabs@mjbright.net>

# NOTE: all RUN commands are executed at build time, look at the output of the "docker build"
#       below and you will see the output of the following line when we build the first time
#       (i.e. when caching is not used):

RUN echo DATE: This build is being done at $(date)
#RUN python ‐‐version

ENV myVar=anythingReally

CMD bash

