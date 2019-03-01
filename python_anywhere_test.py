import requests

my_domain = 'octokatt.pythonanywhere.com'
username = 'octokatt'
token = '9025a4683dfe2cd3b1d3470fdcb9d8b7ce9d5407'

response = requests.post(
  'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
      username=username, domain=my_domain
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('All OK')
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
                        