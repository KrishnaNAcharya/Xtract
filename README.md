# Xtract
This project aims at providing statistical insights to the users from their datasets.
The datasets are processed by the python scripts at the backend and the results are sent back to the user.
These results contain information describing the dataset.

## Steps to run
Firstly, clone this repository
```bash
git clone https://github.com/AvyayNayak/Xtract.git
```
Ensure that there is a Python installed on your device.
### Install dependencies
Run these commands on your terminal
```bash
npm i
```
```bash
pip install numpy scipy matplotlib pandas seaborn
```
### To run the web app, 
```bash
node index.js
```

## Steps to run using Docker
###Build the docker image
```bash
docker build -t *image-name* .
```
### Check if the image was created 
```bash
docker images
```
### Run the Docker image
```bash
docker run -p 5173:5173 *image-name*
```
## How to update code
Create a new branch with an appropriate name and work on that branch.
Follow the commit message semantics mentioned [here](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)
