# Use an official node runtime as a parent image
FROM node:20-slim

# Update and install security updates
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application's code
COPY . .

# Start the app
CMD [ "npm", "start" ]
