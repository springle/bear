FROM node:8.2.1
RUN mkdir /code
WORKDIR /code
ADD package.json /code
RUN npm install >/dev/null 2>/dev/null
ADD . /code/
