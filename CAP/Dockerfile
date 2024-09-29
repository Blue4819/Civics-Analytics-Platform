# Step 1: Use an official Node.js image from DockerHub as the base image
FROM node:16-alpine

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the package.json and package-lock.json files to the container
COPY package.json ./

# Step 4: Install dependencies (this will cache the 'node_modules' layer for faster builds)
RUN npm install

# Step 5: Copy the rest of the application code to the container
COPY . .

# Step 6: Build the React app
RUN npm run build

# Step 7: Use an official NGINX image to serve the built React app
FROM nginx:alpine

# Step 8: Copy the built React app to the NGINX default directory
COPY --from=0 /app/build /usr/share/nginx/html

# Step 9: Expose port 80 to allow external traffic to the container
EXPOSE 80

# Step 10: Start NGINX when the container runs
CMD ["nginx", "-g", "daemon off;"]
