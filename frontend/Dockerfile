FROM 17-alpine3.12

WORKDIR /frontend

COPY package.json ./
COPY yarn.lock ./

RUN yarn

COPY . ./

CMD ["yarn", "start"]