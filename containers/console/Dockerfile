FROM node:lts

WORKDIR /git/console

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["npm", "run", "dev"]
