FROM python:latest

COPY --from=node /usr/local/bin/node /usr/local/bin/
COPY --from=node /usr/local/lib/node_modules/ /usr/local/lib/node_modules/

RUN ln -s /usr/local/bin/node /usr/local/bin/nodejs \
  && ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
  && ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npx



# install the latest nodejs & npm
RUN apt-get update \
    && apt-get install -y nodejs \
       npm \
    && apt-get clean

RUN npm install n -g
RUN n 18.16.0


# # install the latest AWS CDK
RUN npm install -g aws-cdk \
    && pip3 install --upgrade aws-cdk.core

# install the latest AWSCLI
# RUN pip3 install awscli --upgrade

WORKDIR /project

RUN npm install \
    typescript@4.4.4 \
    aws-cdk@2.27.0 \
    ts-node@10.8.1

ENTRYPOINT [ "/project/entrypoint.sh" ]