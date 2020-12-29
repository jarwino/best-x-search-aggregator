import re
import bs4

# Regular expression for valid list item
VALID_LIST_ITEMS = ['>[\\s]*([0-9]+[\\.\\)]\\s[a-zA-Z0-9\\.\\s\\(\\)]+)<\\/',
                    '>[\\s]*([0-9]+[\\.\\)]\\s.*)<\\/a']


def parse_html(html):
    pattern = re.compile("|".join(VALID_LIST_ITEMS))
    best_list = [remove_tags("".join(x)) for x in re.findall(pattern, html)]
    if not best_list:
        soup = bs4.BeautifulSoup(html, 'lxml')
        found = soup.select('h3')
        best_list = [x.text.strip() for x in found]
    return best_list


# TODO: remove, for debugging only
def parse_html_debug(html):
    with open('tmp.html', 'w') as tmp:
        tmp.write(html)
    pattern = re.compile("|".join(VALID_LIST_ITEMS))
    best_list = [remove_tags("".join(x)) for x in re.findall(pattern, html)]
    if not best_list:
        soup = bs4.BeautifulSoup(html, 'lxml')
        found = soup.select('h3')
        best_list = [x.text.strip() for x in found]
    return best_list


def remove_tags(item):
    return bs4.BeautifulSoup(item, "lxml").text
