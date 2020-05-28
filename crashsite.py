import requests
url = "http://ncert.nic.in/"  #this is a sample wesite. you can put any website of your wish, replacing the given website.
c=1
while c>0:
  requests.get(url)
  print(c)
  c+=1
