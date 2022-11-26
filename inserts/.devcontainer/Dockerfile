FROM ruby:3.1-bullseye
RUN mkdir -p /workspaces/{{cookiecutter.project_name}}

RUN apt update \
    && apt install --assume-yes --no-install-recommends \
    mariadb-server
