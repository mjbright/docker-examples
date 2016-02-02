
FROM ubuntu

MAINTAINER "Docker Labs" <dockerlabs@mjbright.net>

#
# Instead of perofmring the followinf commands individually which
# involves creating a separate image layer for each RUN command:
#   RUN apt-get update
#   RUN apt-get -y -q upgrade
#   RUN rm -rf /var/lib/apt/lists/*

# Here we combine the update, upgrade and cleanup steps into one command
# - This produces less image layers (better for disk space and performance)
# - This keeps image smaller by removing temporary files in the same layer
#     If we performed update/upgrade and then rm as a separate step there would
#     be an intermediate layer including those files, making the overall image larger.
#

RUN apt-get update && apt-get -y -q upgrade && rm -rf /var/lib/apt/lists/*

