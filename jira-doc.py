from __future__ import print_function
from collections import Counter
from jira import JIRA
from datetime import datetime, timedelta
import json
import ast
import re

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
check_sprint = jira.search_issues('project=JD and status="In progress"')
sprint = ''
status = ''
for x in check_sprint:
    if status is '':
        check2 = x.fields.customfield_10010[0]
        check3 = '['+check2.split('[')[1] 
        result = re.search('state=(.*),', check3)    
        status = result.group(1).split(',')[0]
        if status == 'ACTIVE':
            if sprint is '':     
                sprint_str = (check3.split('name=')[1])
                sprint = sprint_str.split(',')[0]
        # else:
        #     raise Exception('01100101 01110010 01110010 01101111 01110010')

        
query_string = ('project=JD and status="Done" and Sprint="' + sprint +'"')
done = jira.search_issues(query_string)
print ('Done')
file = open("output.txt", "w")
file.write('Done \n')
for x in done:
    # update_date = x.raw['fields']['updated']
    # update_date = update_date.split('.', 1)[0]
    # then = datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%S")
    # if then > datetime.now() - timedelta(days = 7):
        if x.raw['fields']['assignee']is None:
            output = (x.raw['fields']['summary'])

            file.write(output.encode('utf-8') + '\n')
        else:            
            output = (x.raw['fields']['summary'] +' '+ x.raw['fields']['assignee']['displayName'])
            # print (x.raw['fields'])
            file.write(output.encode('utf-8') + '\n')
query_string = ('project=JD and status="In progress" and Sprint="' + sprint +'"')
inprogress = jira.search_issues(query_string)
print ('In progress')
file.write('In progress \n')
for x in inprogress:
    # update_date = x.raw['fields']['updated']
    # update_date = update_date.split('.', 1)[0]
    # then = datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%S")
    # if then > datetime.now() - timedelta(days = 7):
        if x.raw['fields']['assignee']is None:
            output = (x.raw['fields']['summary'])

            file.write(output.encode('utf-8') + "\n")
        else:            
            output = (x.raw['fields']['summary'] +' '+ x.raw['fields']['assignee']['displayName'])

            file.write(output.encode('utf-8') + "\n")

query_string = ('project=JD and status="To do" and Sprint="' + sprint +'"')
todo = jira.search_issues(query_string)
print ('To do')
file.write('To do \n')
for x in todo:
    # update_date = x.raw['fields']['updated']
    # update_date = update_date.split('.', 1)[0]
    # then = datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%S")
    # if then > datetime.now() - timedelta(days = 7):
        if x.raw['fields']['assignee']is None:
            output = (x.raw['fields']['summary'])

            file.write(output.encode('utf-8') + "\n")
        else:            
            output = (x.raw['fields']['summary'] +' '+ x.raw['fields']['assignee']['displayName'])

            file.write(output.encode('utf-8') + "\n")
file.close()
