# Shared image, envs, packages for both devcontainer & prod.
FROM ruby:3.2-bullseye

# Temporary multi-platform SAM CLI install method.
# https://github.com/aws/aws-sam-cli/issues/3908
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN apt-get install -y pip && pip install aws-sam-cli

# Local devcontainer Codespaces compatibility.
RUN apt update
RUN mkdir -p /workspaces/{{cookiecutter.project_name}}
ENV BUNDLE_IGNORE_CONFIG=1
ENV BUNDLE_PATH=./vendor/bundle
ENV BUNDLE_CACHE_PATH=./vendor/cache
