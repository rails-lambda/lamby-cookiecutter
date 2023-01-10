# Shared image, envs, packages for both devcontainer & prod.
FROM ruby:3.1-bullseye

# Local devcontainer Codespaces compatibility.
RUN apt update
RUN mkdir -p /workspaces/{{cookiecutter.project_name}}
ENV BUNDLE_IGNORE_CONFIG=1
ENV BUNDLE_PATH=./vendor/bundle
ENV BUNDLE_CACHE_PATH=./vendor/cache
HEALTHCHECK CMD docker info
