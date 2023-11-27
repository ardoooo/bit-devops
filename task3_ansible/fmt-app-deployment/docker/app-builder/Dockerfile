FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y openssh-client ansible sshpass docker.io

COPY ./ansible /ansible

WORKDIR /ansible

CMD ["ansible-playbook", "-i", "inventory.cnf", "playbook.yml"]
