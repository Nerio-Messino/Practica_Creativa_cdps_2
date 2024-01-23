FROM node:16
WORKDIR /opt/microservices
COPY package.json .
COPY ratings.js .
ENV SERVICE_VERSION=v1
RUN npm install
EXPOSE 9080
CMD ["node", "ratings.js", "9080"]