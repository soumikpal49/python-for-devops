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

sorted_urls = sorted(
    url_count.items(),
    key=operator.itemgetter(1),
    reverse=True
)

print('2nd Min Occurance:')
print(sorted_urls[-2][0], "(", sorted_urls[-2][1], "occurrences)")

print('-----------------------------------------------------------------')

print('2nd Highest Occurance:')
print(sorted_urls[1][0], "(", sorted_urls[1][1], "occurrences)")

print('-----------------------------------------------------------------')

print('12th Occurance:')
print(sorted_urls[11][0], "(", sorted_urls[11][1], "occurrences)")

print('-----------------------------------------------------------------')

print('First 15 occurance:')
N = 15
for i in range(N):
  print(sorted_urls[i][0], "(", sorted_urls[i][1], "occurrences)")

print('-----------------------------------------------------------------')

#print('sorted urls:')
#print(sorted_urls)
