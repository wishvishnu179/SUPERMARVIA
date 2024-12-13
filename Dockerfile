FROM node:16

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080 # <--- Expose the correct port
CMD ["npm", "start"]
