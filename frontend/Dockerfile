FROM node:16.13.1

WORKDIR /frontend

COPY package.json ./
COPY yarn.lock ./

RUN yarn install --frozen-lockfile

COPY . ./

CMD ["yarn", "start"]