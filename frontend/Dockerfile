FROM node:17

WORKDIR /frontend

COPY package.json ./
COPY yarn.lock ./

RUN yarn install --frozen-lockfile

COPY . ./

CMD ["yarn", "start"]