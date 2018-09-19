# Jira Report

Python script which is pulling data from Jira.

## Getting Started

These instructions will allow you to get informations directly from jira to save your time while filling up report next time.

### TODO

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

### Next to do

* Have to add possibility of adding Done jobs from last 2 days of past sprint.
