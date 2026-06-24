import requests
import operator

file_url = "https://public.karat.io/content/urls2.txt"
response = requests.get(file_url)
urls = response.text.splitlines()
#print(urls)

# Count URLS
url_count = {}
for url in urls:
  if url in url_count:
    url_count[url] += 1
  else:
    url_count[url] = 1

#print(url_count)

# Print top N URLS
max_url = ""
max_count = 0

for url in url_count:
  if url_count[url] > max_count:
    max_count = url_count[url]
    max_url = url

#print(max_url, "(", max_count, "occurrences)")

sorted_urls = sorted(
    url_count.items(),
    key=operator.itemgetter(1),
    reverse=True
)

N = 15
for i in range(N):
  print(sorted_urls[i][0], "(", sorted_urls[i][1], "occurrences)")
