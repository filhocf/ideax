FROM python:alpine

ARG VERSION=master

RUN \
    apk add --no-cache unzip wget  ca-certificates gcc openldap-dev binutils-libs binutils gmp isl libgomp libatomic libgcc pkgconf pkgconfig mpfr3 mpc1 libstdc++ libc-dev musl-dev mariadb-dev

RUN \
    mkdir /var/www; \
    mkdir /var/log
    cd /var/www; \
    wget -O ideax.tar.gz https://github.com/filhocf/ideax/archive/${VERSION}.tar.gz; \
    tar xf ideax.tar.gz; \
    mv ideax-master ideax; \
    rm ideax.tar.gz; \
    cd ideax; \
    pip install -r requeriments.txt; \
    python manage.py collectstatic --no-input; \

WORKDIR /var/www/ideax

COPY ./entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

CMD []
