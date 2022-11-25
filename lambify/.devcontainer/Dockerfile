FROM ruby:3.1-bullseye
RUN mkdir /workspaces

RUN apt update \
    && apt install --assume-yes --no-install-recommends \
    mariadb-server
