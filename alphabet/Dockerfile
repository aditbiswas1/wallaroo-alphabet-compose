FROM wallaroo-labs-docker-wallaroolabs.bintray.io/release/wallaroo:0.4.2

RUN env-setup

ADD . /code

WORKDIR /code

EXPOSE 10000-50000

ENTRYPOINT ["/bin/sh", "-c", "\"${*}\""]