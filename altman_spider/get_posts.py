import requests
from bs4 import BeautifulSoup


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print('Error cant get_page')
        return None


def get_posts_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    posts_link = [a['href'] for a in soup.select('article header h2 a')]
    return posts_link


def get_article(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('article').find('header').find('h2').find('a').text
    paragraphs = [p.text for p in soup.find(
        'div', {'class': 'posthaven-post-body'}).find_all('p')]
    return title, paragraphs


def main():
    page = 1
    while True:
        url = 'https://blog.samaltman.com/?page=' + str(page)
        html = get_page(url)
        print('正在输出' + url)
        page += 1
        # 得到本页中所有文章的链接
        posts_link = get_posts_link(html)
        # 遍历所有文章
        for post_link in posts_link:
            print(post_link)
            html = get_page(post_link)
            article = get_article(html)
            with open('./posts/' + article[0] + '.txt', 'w', encoding='utf-8') as f:
                for paragraph in article[1]:
                    f.write(paragraph + '\n')


if __name__ == '__main__':
    main()
