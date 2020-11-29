FROM mongo:4.2.1

COPY /docker/mongodb/custom-mongo-user.sh /docker-entrypoint-initdb.d/

RUN chmod 0755 /docker-entrypoint-initdb.d/custom-mongo-user.sh

