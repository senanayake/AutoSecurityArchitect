FROM amazonlinux:latest
# Update the package manager and install necessary tools
RUN yum install python -y && yum install pip -y && yum install vim -y  && yum install tmux -y
WORKDIR /opt/app
COPY requirements.txt /opt/app

