# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package*.json files to the working directory
COPY package*.json ./

# Install the dependencies
RUN npm install --verbose
RUN npm install --legacy-peer-deps
RUN npm install react-router-dom chart.js

# Copy the application code to the working directory
COPY . .

# Expose the port that the application will run on
EXPOSE 3000

# Run the command to start the development server
CMD ["npm", "start"]