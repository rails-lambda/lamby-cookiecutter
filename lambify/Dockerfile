FROM public.ecr.aws/lambda/ruby:2.7
ARG RAILS_ENV
ENV RAILS_ENV=$RAILS_ENV
COPY . .
CMD ["app.handler"]
