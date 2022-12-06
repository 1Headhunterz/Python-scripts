import requests
 
def download_url(url):
  # assumes that the last segment after the / represents the file name
  # if the url is http://abc.com/xyz/file.txt, the file name will be file.txt
  file_name_start_pos = url.rfind("/") + 1
  file_name = url[file_name_start_pos:]
 
  r = requests.get(url, stream=True)
  if r.status_code == requests.codes.ok:
    with open(file_name, 'wb') as f:
      for data in r:
        f.write(data)
 
# download a sngle url
# the file name at the end is used as the local file name
download_url("https://index2.shinobicloud.cf/0:/BOT2_Upload/")