# getting around 403:
# inspect requests, copy useragent and pass as -ua arg
# e.g. Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36

import getopt
import requests
import sys
from bs4 import BeautifulSoup # pip install beautifulsoup4
from urllib.parse import urlparse

if __name__ == "__main__":
  try:
      opts, args = getopt.getopt(sys.argv[1:], "u:ua:", ["url="])
  except getopt.GetoptError as err:
      print(err)
      sys.exit()
  for param, val in opts:
      if param in ('-u', '--url'):
          try:
              url = val
              assert(urlparse(url))
          except AssertionError:
              print("URL (e.g. https://www.google.com) must be valid. Make sure argument is -u or --url.")
              sys.exit()
      else:
          print("--url (e.g. https://www.google.com) are the only possible commandline arguments.")
          sys.exit()
  try:
      print("Getting HTML document for url: " + url)
  except NameError:
      print("--url (e.g. https://www.google.com) is a required commandline argument.")
      sys.exit()

  headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
  }

  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.content, "html.parser")
  print(soup.prettify())

