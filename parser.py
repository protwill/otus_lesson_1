from typing import List, Dict

import requests
import click
from bs4 import BeautifulSoup

from Writer.UrlWriter import ScreenUrlWriter, FileUrlWriter


def validate_url(url: str, base_url: str) -> str:
    if not url.endswith("/"):
        url = f"{url}/"

    if url.startswith("/"):
        url = base_url + url

    return url


def get_html(url: str, timeout: int) -> str:
    try:
        response = requests.get(url, timeout=timeout)
    except BaseException:
        return ""

    return response.text


def find_links(html: str, base_url: str) -> List[str]:
    soup = BeautifulSoup(html, "html.parser")
    links = soup.findAll(name="a", href=True)

    return [validate_url(link["href"], base_url) for link in links]


def get_urls(url_storage: Dict, recursion_dept: int, timeout: int, limit: int, dept_level=0) -> None:
    if dept_level == recursion_dept:
        return None

    for base_urls in url_storage.keys():
        html = get_html(base_urls, timeout)
        urls = find_links(html, base_urls)

        i = 0
        for url in urls:
            i += 1
            if (limit > 0) and (i > limit):
                break

            url_storage[base_urls][url] = dict()

        get_urls(url_storage[base_urls], recursion_dept, timeout, limit, dept_level + 1)


@click.command()
@click.argument("url", required=1)
@click.option("--file", default="", help="Path to output file. If undefined then output to the screen.")
@click.option("--recursion_depth", default=1, help="Depth of recursion for nested links. Default is 1.")
@click.option("--timeout", default=1, help="Connection timeout in seconds for get URL method. Default is 1")
@click.option("--limit", default=0, help="Limit link per page, if 0 then no limit. Default is 0.")
def main(url: str, file: str, recursion_depth: int, timeout: int, limit: int) -> None:
    urls_storage = dict()
    urls_storage[validate_url(url, "")] = {}

    get_urls(urls_storage, recursion_depth, timeout, limit)

    if file == "":
        writer = ScreenUrlWriter(urls_storage)
    else:
        writer = FileUrlWriter(urls_storage, file)
    writer.write()


if __name__ == "__main__":
    main()
