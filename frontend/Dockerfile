# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /frontend

# add `/app/node_modules/.bin` to $PATH
ENV PATH /frontend/node_modules/.bin:$PATH

# install and cache app dependencies
#COPY node_modules /frontend/
COPY package.json /frontend/package.json
RUN npm install
RUN npm install @vue/cli@5.0.8 -g

# start app
CMD ["npm", "run", "serve"]
