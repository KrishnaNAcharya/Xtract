# Xtract
This project aims at providing statistical insights to the users from the datasets they provide as input.
The dataset recieved from the user is processed by the python scripts at the backend.
The results of the analysis so obtained are sent back to the user.
These results include the statistical data and graphs describing the dataset.

## Steps to run
Firstly, clone this repository in your desired directory
```bash
git clone https://github.com/AvyayNayak/Xtract.git
```
Also, ensure that there is a Python executable installed on your device.
### Install dependencies
Run this command on your terminal
```bash
npm i
```
### Install python dependencies
```bash
pip install numpy
```
```bash
pip install scipy
```
```bash
pip install matplotlib
```
```bash
pip install pandas
```
```bash
pip install seaborn
```
### To run the web app, 
```bash
node index.js
```
## How to update code
If working on a new feature

Create new branch and work in that preferably named `feat/featureName`

```bash
git add filename
#or
git add .

git commit -m "sutiable msg"
```

#### Note: Ignore this warning for now, re-run the command that created this
`warning: in the working copy of 'tsconfig.json', LF will be replaced by CRLF the next time Git touches it`

```bash
git checkout -b branchname
```

To push local branch to remote

```bash
git push -u origin branchname
```
