FROM node

RUN yarn global add parcel-bundler

EXPOSE 1234
EXPOSE 33187
WORKDIR /git/map

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["npm", "run", "dev"]
