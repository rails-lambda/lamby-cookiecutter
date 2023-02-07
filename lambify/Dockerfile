# Shared image, envs, packages for both devcontainer & prod.
FROM ruby:3.2-bullseye

# Install the AWS Lambda Runtime Interface Client & Crypteia for secure SSM-backed envs.
RUN gem install 'aws_lambda_ric'
COPY --from=ghcr.io/customink/crypteia-extension-debian:1.1.0 /opt /opt
ENTRYPOINT [ "/usr/local/bundle/bin/aws_lambda_ric" ]
ENV LD_PRELOAD=/opt/lib/libcrypteia.so

# Create a secure user for prod and app directory.
RUN mkdir /app \
    && groupadd -g 10001 app \
    && useradd -u 10000 -g app app \
    && chown -R app:app /app
USER app
WORKDIR "/app"

# Copy prod application files and set handler.
ENV BUNDLE_IGNORE_CONFIG=1
ENV BUNDLE_PATH=./vendor/bundle
ENV BUNDLE_CACHE_PATH=./vendor/cache
ENV RAILS_SERVE_STATIC_FILES=1
COPY . .
CMD ["config/environment.Lamby.cmd"]
