FROM bitnami/debian-base-buildpack:latest

RUN /sbin/groupadd -g 808 pygooglevoice
RUN /sbin/useradd -c "user" -d /home/pygooglevoice -g 808 -m pygooglevoice

RUN yum --noplugins install -y \
      python \
      python-setuptools \
      && yum clean all

RUN mkdir -p /pygooglevoice

COPY . /home/pygooglevoice

WORKDIR /home/pygooglevoice

RUN python setup.py install

VOLUME /home/pygooglevoice
USER pygooglevoice
