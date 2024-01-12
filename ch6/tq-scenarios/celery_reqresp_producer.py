from celery_worker import write_logitem

response = write_logitem('Subscription', 'New subscription entered for J. Watson')
print('Producer - received response:', response)
