FROM ubuntu

RUN apt-get update && apt-get install -y \
  npm

RUN npm install -g \
  parcel-bundler

EXPOSE 1234
EXPOSE 33187
WORKDIR /git/map

CMD ["npm", "run", "dev"]
