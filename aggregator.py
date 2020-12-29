import argparse
import requests
from googleapi import google

import best_list_parser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Aggregate "best <X>" search results')
    parser.add_argument('query', help='query to search for')
    args = parser.parse_args()
    best_lists = []
    for result in google.search(f"best {args.query}"):
        url = result.link
        html = requests.get(url).text
        # TODO: remove, for debugging only
        if 'brad-pitt-best-performances' in url:
            best_list = best_list_parser.parse_html_debug(html)
        else:
            best_list = best_list_parser.parse_html(html)
        ####
        if best_list:
            print(
                "-----------------------------------------------------------------------")
            print(url)
            for item in best_list:
                print(f">>> {item}")
        best_lists.append(best_list)
