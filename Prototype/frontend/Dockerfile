# Use official Node.js image (Alpine for small size)
FROM node:20-alpine

# Set working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache bash

# Copy package.json and package-lock.json first for better caching
COPY package*.json ./

# Remove old dependencies and clean npm cache
RUN rm -rf node_modules package-lock.json && npm cache clean --force

# Install project dependencies
RUN npm install --legacy-peer-deps

# Copy the entire project into the container
COPY . .

# Expose the frontend development server port
EXPOSE 5173

# Start the Vue app using Vite
CMD ["npm", "run", "dev"]