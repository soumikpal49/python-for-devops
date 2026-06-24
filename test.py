from collections import Counter
from urllib.request import urlopen

def most_pop_url(log_file_url):
  with urlopen(log_file_url) as response:
    lines = response.read().decode("utf-8").splitlines()

  url_count = Counter(lines)

most_common_url, count = url_count.most_common_url(1)[0]

print (f"{most_common_url} ({count} occurances)")

logfile1 = "url2.txt"
logfile2 = "single_url2.txt"

most_popular_url(logfile1)
most_popular_url(logfile2)
