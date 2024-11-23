# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package*.json files to the working directory
COPY package*.json ./

# Install the dependencies
RUN npm install --verbose
RUN npm install --legacy-peer-deps

# Copy the application code to the working directory
COPY . .
COPY ../National\ Disasters/ /app/data/nationa_disasters/
COPY ../Economic\ Deficits/ /app/data/economic_deficits/

# Expose the port that the application will run on
EXPOSE 3000

# Run the command to start the development server
CMD ["npm", "start"]