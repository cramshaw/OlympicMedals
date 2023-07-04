FROM node:18.16-slim as react

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . ./

# Only for local dev
ENTRYPOINT [ "npm" , "run"]
CMD ["dev"]