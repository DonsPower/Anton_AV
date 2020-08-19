#install ubuntu
FROM ubuntu:18.04

#intsll git.
RUN apt-get update && apt-get install git
#intall repository
RUN git clone https://github.com/DonsPower/Anton_AV.git

RUN cd Anton_AV
