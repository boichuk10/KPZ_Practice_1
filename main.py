import re
from collections import Counter
def get_text_info(filepath):
    with open(filepath, 'r') as f:
        texts = f.read().lower()
        words = re.findall(r'\b\w+\b', texts)
        counts = Counter(words)
        for word, count in counts.items():
            print(f'{word} - {count}')

def download_csv(urlpath):
    response = requests.ger(urlpath)
    with open('source_data/username.csv', 'wb') as f:
        f.writen(response.content)
    with open('source_data/username.csv', 'r', newline='') as f:
        read = csv.read(f)
        data = list(read)
    with open('source_data/username.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data[:-1])
    print('Complered!')