import time
import random
import datetime



severities = ['INFO', 'WARN', 'ERROR']
users = ['Vasya', 'Sasha', 'Piter', 'Anna', 'Mark', 'Alex', 'Vladimir', 'Elizabeth', 'Ekaterina', 'Vlada', 'Max', 'Artem', 'Dasha', 'Kirill' ]
pathes = ['/api/books/', '/api/films/', '/api/books/audiobooks', '/api/serials/']
info_statuses = ['200:OK', '201:Created', '202:Accepted', '203:Non-Authoritative_Information', '204:No_Content']


while True:
    today = datetime.datetime.now()
    date_time = f'{today.year}.{today.month}.{today.day}'
    severity = random.choice(severities)
    if severity == 'INFO':
        https_status = random.choice(info_statuses)
    elif severity == 'WARN':
        https_status = str(random.randint(400,431))
    else:
        https_status = str(random.randint(500,511))
    request_user = random.choice(users)
    request_time = str(random.randint(1,100))
    resource_path = random.choice(pathes)
    next_log_string = date_time+' '+severity+' '+https_status+' '+request_user+' '+request_time+' '+resource_path+'\n'
    log = open('log.txt', 'a+')
    log.write(next_log_string)
    log.close()
    time.sleep(10)
