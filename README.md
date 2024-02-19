# Xtract
This project aims at providing statistical insights to the users from the datasets they provide as input.
The dataset recieved from the user is processed by the python scripts at the backend.
The results of the analysis so obtained are sent back to the user.
These results include the statistical data and graphs describing the dataset

## Clone the repository
```bash
git clone https://github.com/AvyayNayak/Xtract.git
```
### Install dependencies
Open your terminal and run this
```bash
npm i
```
For the python scripts, a virtual environment already exists within the repository. Simply run this command to it.
```bash
.\env\Scripts\activate
```
For those who run into an unauthorized access error, run the following command to bypass the execution policy temporarily:
```bash
Set-ExecutionPolicy Bypass -Scope Process
```
If you want to make a permanent change to the execution policy, run this
```bash
Set-ExecutionPolicy Bypass -Scope CurrentUser
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
