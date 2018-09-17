from __future__ import print_function
from collections import Counter
from jira import JIRA
from datetime import datetime, timedelta


with open('creds.txt') as f:
  creds = [x.strip().split(':') for x in f.readlines()]
for username,password in creds:
    with open('config.yaml') as l:
        url = l.readlines()
    for server in url:
        options = {
            'server': server
            }
jira = JIRA(options, basic_auth = (username, password))

done = jira.search_issues('project=JD and status="Done" and Sprint="Sprint 12"')
print ('Done')
file = open("output.txt", "w")
file.write('Done \n')
for x in done:
    update_date = x.raw['fields']['updated']
    update_date = update_date.split('.', 1)[0]
    then = datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%S")
    if then > datetime.now() - timedelta(days = 7):
        if x.raw['fields']['assignee']is None:
            output = (x.raw['fields']['summary'])
            
            file.write(output.encode('utf-8') + '\n')
        else:            
            output = (x.raw['fields']['summary'] +' '+ x.raw['fields']['assignee']['displayName'])
            
            file.write(output.encode('utf-8') + '\n')

inprogress = jira.search_issues('project=JD and status="In progress" and Sprint="Sprint 12"')
print ('In progress')
file.write('In progress \n')
for x in inprogress:
    update_date = x.raw['fields']['updated']
    update_date = update_date.split('.', 1)[0]
    then = datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%S")
    if then > datetime.now() - timedelta(days = 7):
        if x.raw['fields']['assignee']is None:
            output = (x.raw['fields']['summary'])
            
            file.write(output.encode('utf-8') + "\n")
        else:            
            output = (x.raw['fields']['summary'] +' '+ x.raw['fields']['assignee']['displayName'])
            
            file.write(output.encode('utf-8') + "\n")

todo = jira.search_issues('project=JD and status="To do" and Sprint="Sprint 12"')
print ('To do')
file.write('To do \n')
for x in todo:
    update_date = x.raw['fields']['updated']
    update_date = update_date.split('.', 1)[0]
    then = datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%S")
    if then > datetime.now() - timedelta(days = 7):
        if x.raw['fields']['assignee']is None:
            output = (x.raw['fields']['summary'])
            
            file.write(output.encode('utf-8') + "\n")
        else:            
            output = (x.raw['fields']['summary'] +' '+ x.raw['fields']['assignee']['displayName'])
            
            file.write(output.encode('utf-8') + "\n")
file.close()
