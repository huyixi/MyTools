import urllib.request
import time

base_url = 'http://www.mofcom.gov.cn/dl/gbdqzn/upload/'
with open('undownload.txt', 'r') as f:
    for line in f:
        url = base_url + line.strip() + '.pdf'
        for i in range(5):
            try:
                urllib.request.urlretrieve(url, line.strip()+'.pdf')
                print(f'Successfully downloaded {line.strip()}.pdf')
                break
            except urllib.error.HTTPError as e:
                print(f'Error: {e.code} - {e.reason}')
                if i < 4:
                    time.sleep(5)
                else:
                    print(f'Failed to download {line.strip()}.pdf')
