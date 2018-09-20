# Jira Report

Python script which is pulling data from Jira.

## Getting Started

These instructions will allow you to get informations directly from jira to save your time while filling up report next time.

### Installation

* Get your private Token for jria from https://id.atlassian.com/manage/api-tokens
* Create file ``creds.txt`` in your git repo dir.
* It should looks like 
```
username:TOKEN
```
* Create file ``config.yaml`` in your git repo dir.
* It should looks like
```
https://jira server
```
### Last Patches

* Added auto sprint detection
* Putted Raport Generator into function
* Added check of fresh sprint
* Added pull of last two days of previous sprint to the section Done
* Added indication of tasks that were included in more than one sprint

### Next to do

* Have to add requirements.txt file to the project. 
