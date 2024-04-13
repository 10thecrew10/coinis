import json, csv

FILE_PATH = 'week-6/files/homework.json'


def read_json_file(filename: str = FILE_PATH):
    with open(FILE_PATH) as f:
        return json.loads(f.read())


def write_json_file(data: dict, filename: str = FILE_PATH):
    with open(FILE_PATH, 'w') as f:
        return json.dump(data, f, indent=4)


def find_article_by_title(title: str):
    js = read_json_file()
    articles = js['data']['articles']
    res = [x for x in articles if x['title'] == title]
    if res:
        return res[0]


def add_comment(article_title: str, comment_title: str, description: str, author: str = 'anonim'):
    js = read_json_file()
    articles = js['data']['articles']

    index = [i for i, x in enumerate(articles) if x['title'] == article_title]
    if not index:
        return
    index = index[0]

    if any(True for x in articles[index]['comments'] if x['title'] == comment_title):
        return

    js['data']['articles'][index]['comments'].append({'title': comment_title, 'author': author, 'description': description})
    write_json_file(js)


def delete_articles_by_title_comment(title: str):
    js = read_json_file()
    articles = js['data']['articles']

    for i, article in enumerate(articles):
        if any(True for x in article['comments'] if x['title'] == title):
            js['data']['articles'][i] = None

    js['data']['articles'] = [x for x in js['data']['articles'] if x is not None]
    write_json_file(js)


def get_comment_by_title(article_title: str, comment_title: str):
    article = find_article_by_title(article_title)
    if not article:
        return

    comment = list(filter(lambda x: x['title'] == comment_title, article['comments']))
    if comment:
        return comment[0]


def get_comments_by_author(author: str):
    js = read_json_file()
    articles = js['data']['articles']
    res = []
    for article in articles:
        comment = list(filter(lambda x: x['author'], article['comments']))
        if comment:
            res += comment
    return res


def get_articles_by_author(author: str):
    js = read_json_file()
    articles = js['data']['articles']
    return [x for x in articles if x['author'] == author]


def write_articles_csv(author: str):
    articles = get_articles_by_author(author)
    articles.sort(key=lambda x: len(x['comments']), reverse=True)
    with open('week-6/files/articles.csv', 'w', newline='', encoding='UTF-8') as f:
        fieldnames = ['title', 'author', 'description', 'category', 'views', 'comments_count']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for article in articles:
            writer.writerow({
                fieldnames[0]: article['title'],
                fieldnames[1]: article['author'],
                fieldnames[2]: article['description'],
                fieldnames[3]: article['category'],
                fieldnames[4]: article['views'],
                fieldnames[5]: len(article['comments'])
            })


def write_articles_json(author: str):
    articles = get_articles_by_author(author)
    articles.sort(key=lambda x: x['views'], reverse=True)
    with open('week-6/files/articles.json', 'w', encoding='UTF-8') as f:
        json.dump(articles, f, indent=4)



# print(find_article_by_title('Innovations in Renewable Energy'))
# print(add_comment('Apple is Listening', 'title1', 'test description 1'))
# print(add_comment('Apple is Listening', 'title2', 'test description 2'))
# delete_articles_by_title_comment('hi')
# print(get_comment_by_title("Apple is Listening 2", 'Nice'))
# print(get_comments_by_author('anonim'))
# print(get_articles_by_author('Marco Arment'))
# write_articles_csv('Marco Arment')
# write_articles_json('Marco Arment')
