FROM node:22-alpine
WORKDIR /srv/app
COPY package.json ./
RUN npm install --omit=dev
COPY dist ./dist
CMD ["npm", "start"]
