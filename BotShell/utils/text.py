import re


def clean_html_markup(text):
    delete_markup = [
        '<s>',
        '</s>',
        '<p>',
        '</p>',
        '<br />',
        '<br/>',
        '<ul>',
        '</ul>',
        '</li>', '<strong>', '</strong>', '<em>', '</em>', '&nbsp;', '&laquo;', '&raquo;', '&mdash;', '<li>', '</a>']

    for markup in delete_markup:
        text = text.replace(markup, '')

    href_re = '<a href=\"[hH][tT][tT][pP][sS]?://(?:[a-zA-Z]|[0-9]|[~$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))' \
              '+\">'

    text = re.sub(href_re, '', text)

    return text

def telegram_markup(text):
    delete_markup = ['<p>', '</p>', '<br />', '<br/>', '<ul>', '</ul>', '</li>']
    text = text.replace('<strong>', '<b>')
    text = text.replace('</strong>', '</b>')
    text = text.replace('<em>', '<i>')
    text = text.replace('</em>', '</i>')
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&laquo;', '"')
    text = text.replace('&raquo;', '"')
    text = text.replace('&mdash;', '-')
    text = text.replace('<li>', '- ')

    for markup in delete_markup:
        text = text.replace(markup, '')

    return text