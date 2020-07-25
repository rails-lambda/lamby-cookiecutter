FROM lambci/lambda:build-ruby2.7

# Ensure shared SAM version.
RUN pip install awscli && \
    pip uninstall --yes aws-sam-cli && \
    pip install aws-sam-cli==v1.0.0

# Node for JavaScript.
RUN curl -sL https://rpm.nodesource.com/setup_12.x | bash - && \
    yum install -y nodejs && \
    curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo && \
    rpm --import https://dl.yarnpkg.com/rpm/pubkey.gpg && \
    yum install -y yarn

# Vim for editing credentials.
RUN yum install -y vim

WORKDIR /var/task
