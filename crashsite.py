import requests
url = "http://ncert.nic.in/"
c=1
while c>0:
  requests.get(url)
  print(c)
  c+=1
