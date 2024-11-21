# Specify the node base image with your desired version
FROM node:20.11.1

# Create app directory
WORKDIR /app

# Install Python dependencies
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment
RUN python3 -m venv /venv

# Ensure the virtual environment is active
ENV PATH="/venv/bin:$PATH"

# Install Python dependencies inside the virtual environment
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install app dependencies for Node.js
COPY package*.json ./
RUN npm install

# Bundle app source
COPY . .

# Expose the port your app runs on
EXPOSE 5173

# Run your app using CMD
CMD ["node", "index.js"]
