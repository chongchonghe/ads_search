#!/usr/bin/env python3
"""
Copy bibtex to clipboard
"""

import sys, os
import subprocess
import ads
import warnings
from argparse import ArgumentParser, RawTextHelpFormatter

def parse_args():

    parser = ArgumentParser(
        description="""
A simple ads parser that works

ads, a simple program that copies bibtex into clipboard. Simply copy
and paste the ApJ/MNRAS style reference (starting from the year) as
arguments. The tracing commas will be ignored. Replace '&' with '\&'
in the journal name. Author: Chong-Chong He (che1234@umd.edu)

Example:
>>> {0} 1955, ApJ, 121, 161
>>> {0} 2002, A\&A, 382, 28
>>> {0} 2002, 'A&A' 382, 28
>>> {0} -w 1955, ApJ, 121, 161""".format(os.path.basename(sys.argv[0])),
        formatter_class=RawTextHelpFormatter)
    # parser.add_argument('-b', type=str, nargs=1, help="bibcode")
    parser.add_argument('year', nargs='?', help="year")
    parser.add_argument('jour', nargs='?', help="journal")
    parser.add_argument('vol', nargs='?', help="volume")
    parser.add_argument('page', nargs='?', help="page")
    parser.add_argument('-w', action='store_true', help="open url in borwser")
    parser.add_argument('-t', action='store_true',
                        help=("run a test, which is equivalent to running "
                              "'ads 1955, ApJ, 121, 161'"))
    return parser.parse_args()

def openads(bibcode):

    url = "https://ui.adsabs.harvard.edu/abs/{}".format(bibcode)
    url = url.replace('&', '\&')
    os.system('open ' + url)

def get_ads(year, jour, vol, page):

    if not year.isdigit():
        print("Invalid YEAR in the input.")
        print("Usage: {} year journal_name volume Page/ID".format(sys.argv[0]))
        return
    if jour=='ApJ' and page[0]=='L':
        jour = 'ApJL'
    if jour=='Science':
        jour = 'Sci'
    papers = ads.SearchQuery(bibstem=jour, year=year, volume=vol, page=page)
    return papers

def adsurl(year, jour, vol, page, is_bibcode=False, openurl=False):

    papers = get_ads(year, jour, vol, page)
    for p in papers:
        warnings.filterwarnings("ignore")
        if openurl:
            openads(p.bibcode)
            return
        bib = p.bibtex if not is_bibcode else p.bibcode
        subprocess.run("pbcopy", universal_newlines=True, input=bib, )
        print('{} copied to clipboard:'.format(
            'bibcode' if is_bibcode else 'bibtex'))
        print()
        print(bib, end='')
        return
    print('Failed to find the bibtex. The following search failed:')
    print(f"ads.SearchQuery(bibstem={jour}, year={year}, "
          "volume={vol}, page={page})")
    print(f"Copy the following texts to ads search bar and have a try:")
    print()
    print(f'bibstem:"{jour}" year:"{year}" volume:"{vol}" page:"{page}"')

def parse_key_words(args):
    return [arg.replace(',', '').replace(' ', '') for arg in args]

def main():
    args = parse_args()
    if args.t:
        args.year = '1955'
        args.jour='ApJ'
        args.vol='121'
        args.page='161'
        print("Doing the test: attempting to search for the following article:")
        print(f"{args.year}, {args.jour}, {args.vol}, {args.page}")
        print("If you see 'bibtex copied to clipboard:' followed by a bibtex "
            "entry of the article, 'The Luminosity Function and Stellar Evolution',"
            " it means the test is successful\n")
    this_args = parse_key_words([args.year, args.jour, args.vol, args.page])
    adsurl(*this_args, openurl=args.w)


if __name__ == "__main__":

    # main(sys.argv)
    exit(main())
