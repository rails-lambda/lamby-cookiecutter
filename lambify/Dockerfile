FROM ruby:3.1-slim-bullseye

RUN gem install 'aws_lambda_ric'

COPY --from=ghcr.io/customink/crypteia-extension-debian:latest /opt /opt
COPY . .

ENV RAILS_SERVE_STATIC_FILES=1

CMD ["app.handler"]
ENTRYPOINT [ "/usr/local/bundle/bin/aws_lambda_ric" ]
