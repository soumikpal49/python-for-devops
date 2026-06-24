import requests

file_url = "https://public.karat.io/content/urls2.txt"

response = requests.get(file_url)

urls = response.text.splitlines()

# Count URLS
url_count = {}
for url in urls:
  if url in url_count:
    url_count[url] += 1
  else:
    url_count[url] = 1
    
N = 15

# Print top N URLS
for i in range(N):
  max_url =
  max count = 0
  
  for url in url_count:
    if url_count[url] > max_count:
      max_count url_count[url]
      max_url = url
      
  print(max_url, "(", max_count, "occurrences)")
  
# Remove it so next highest can be found
  del url_count [max_url]
