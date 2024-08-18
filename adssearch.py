#!/usr/bin/env python3

import sys, os
from argparse import ArgumentParser, RawTextHelpFormatter

# SORT = "date"
SORT = "citation_count"

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

def parse_key_words(args):
    return [arg.replace(',', '').replace(' ', '') for arg in args]

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
    parser.add_argument('year', help="year")
    parser.add_argument('jour', help="journal")
    parser.add_argument('vol', help="volume")
    parser.add_argument('page', help="page")
    parser.add_argument('-w', action='store_true', help="open url in borwser")
    parser.add_argument('-t', action='store_true',
                        help=("run a test, which is equivalent to running "
                              "'ads 1955, ApJ, 121, 161'"))
    return parser.parse_args()

def parse_args_v2():

    parser = ArgumentParser(
        description="""
A simple ads parser that works.

Can do one of the following:
1. Find the url of a paper on ADS given an ApJ/MNRAS style bibliography
2. Find the url of a paper on ADS given an author and year
3. Add a article to BibDesk given an article identifier

Author: Chong-Chong He (che1234@umd.edu)

Examples:
>>> {0} -ay Salpeter55
>>> {0} -ay Salpeter1955
>>> {0} -ay Salpeter 1955
>>> {0} -b 1955, ApJ, 121, 161
>>> {0} -a 1955ApJ...121..161S""".format(os.path.basename(sys.argv[0])),
        formatter_class=RawTextHelpFormatter)
    # ["bibliography", 'year', 'vol', 'page']
    parser.add_argument('-b', nargs=4,
                        help="bibliography. Open a browser tab and direct to an ADS page "
                        "of the given article specified by a ApJ/MNRAS style"
                        " bibliography. "
                        "The tracing commas will be ignored. Replace '&' "
                        "with '\&' in the journal name. e.g.\n"
                        "\tads -b 1955, ApJ, 121, 161\n"
                        "\tads -b 2002, A\&A, 382, 28"
                        )
    parser.add_argument('-ay', nargs='+',
                        help="author year. Open a browser tab and direct to an ADS page "
                        "of the given article specified by first author and "
                        "year. Two-digit number are idendified as 19xx if bigger"
                        " than 50 else as 20xx. "
                        "e.g.\n"
                        "\tads -ay Salpeter 1955\n"
                        "\tads -ay Salpeter1955\n"
                        "\tads -ay Salpeter55.\n")
    parser.add_argument('-a', type=str,
                        help="article identifier. Add article to bibdesk. Accept bibcode/arxiv "
                        "id/doi as the article_identifier. Equivalent to "
                        "'ads2bibdesk ARTICLE_IDENTIFIER'. e.g.\n"
                        "\tads -a 1955ApJ...121..161S")
    parser.add_argument('-nob', action='store_true',
                        help="no browser. Toggle off 'open url in borwser'")
    parser.add_argument('-t', action='store_true',
                        help=("test. Run a test: 'ads -b 1955, ApJ, 121, 161'"))
    return parser, parser.parse_args()


def parse_args_v3():

    parser = ArgumentParser(
        description="""
A simple ads parser that works.

Can do one of the following:
1. Find the url of a paper on ADS given an ApJ/MNRAS style bibliography
2. Find the url of a paper on ADS given an author and year
3. Add a article to BibDesk given an article identifier

Author: Chong-Chong He (che1234@umd.edu)

Kinds
- ay: author year. Open a browser tab and direct to an ADS page of the given article specified by first author and year. Two-digit number are idendified as 19xx if bigger than 50 else as 20xx
- r: "bibliography. Open a browser tab and direct to an ADS page of the given article specified by a ApJ/MNRAS style bibliography. The tracing commas will be ignored. Replace '&' with '\&' in the journal name. e.g."
- a: ads article identifier. "article identifier. Add article to bibdesk. Accept bibcode/arxiv id/doi as the article_identifier. Equivalent to 'ads2bibdesk ARTICLE_IDENTIFIER'."
    
Examples:
>>> {0} ay Salpeter55
>>> {0} ay Salpeter1955
>>> {0} ay Salpeter 1955
>>> {0} r 1955, ApJ, 121, 161
>>> {0} r 2002, A\&A, 382, 28
>>> {0} a 1955ApJ...121..161S""".format(os.path.basename(sys.argv[0])),
        formatter_class=RawTextHelpFormatter)
    # ["bibliography", 'year', 'vol', 'page']
    parser.add_argument('kind', help="one of [ay, r, b]")
    parser.add_argument('params', help="parameters", nargs="+")
    # parser.add_argument('-nob', action='store_true',
    #                     help="no browser. Toggle off 'open url in borwser'")
    # parser.add_argument('-t', action='store_true',
    #                     help=("test. Run a test: 'ads -b 1955, ApJ, 121, 161'"))
    return parser, parser.parse_args()

def validate_ads(year, jour, vol, page):
    if not year.isdigit():
        print("Invalid YEAR in the input.")
        print("Usage: {} year journal_name volume Page/ID".format(sys.argv[0]))
        return
    if jour=='ApJ' and page[0]=='L':
        jour = 'ApJL'
        page = page[1:]
    if jour=='Science':
        jour = 'Sci'
    if '&' in jour:
        jour = jour.replace('&', "%26")
    if 'nat' in jour.lower():
        jour = "Natur"
    return {"year": year, "jour": jour, "vol": vol, "page": page}

def clean_args(arg):
    for it in arg.keys():
        arg[it] = arg[it].replace(',', '').replace(' ', '')
        pass
    return arg

def geturl(arg):
    theurl = f"https://ui.adsabs.harvard.edu/search/q=bibstem%3A{{jour}}%20year%3A{{year}}%20volume%3A{{vol}}%20page%3A{{page}}&sort={SORT}%20desc%2C%20bibcode%20desc&p_=0"
    return theurl.format(**arg)

def main_v2():
    # if len(sys.argv) == 2:
    #     if sys.argv[1][0] != '-':
    #         sys.exit(os.system("ads2bibdesk " + sys.argv[1]))
    # # arg = clean_args(parse_args())
    parser, parse = parse_args_v2()
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(2)
    if parse.t:
        args = {"year": "1955", "jour": "ApJ", "vol": "121", "page": "161"}
        print("Parsed input:", args)
        print("opening " + geturl(args))
        if not parse.nob:
            os.system("open " + geturl(args))
            print("This should open a brower tab and direct to Salpeter's "
                  "1955 paper on ADS")
    if parse.a is not None:
        sys.exit(os.system("ads2bibdesk " + parse.a))
        return
    if parse.b is not None:
        args = {"year": parse.b[0], "jour": parse.b[1], "vol": parse.b[2], "page": parse.b[3]}
        args = clean_args(args)         # dict
        args = validate_ads(**args)     # dict
        print("Parsed input:", args)
        print("opening " + geturl(args))
        if not parse.nob:
            os.system("open " + geturl(args))
        # print(get_ads(**arg))
    if parse.ay is not None:
        theauthor = parse.ay[0]
        if theauthor[-2:].isdigit():
            if theauthor[-4:].isdigit():
                author = theauthor[:-4]
                year = theauthor[-4:]
            else:
                author = theauthor[:-2]
                year = int(theauthor[-2:])
                year = 1900 + year if year >= 50 else 2000 + year
        else:
            year = parse.ay[1]
        print("Parsed input: author = {}, year = {}".format(author, year))
        # url = "https://ui.adsabs.harvard.edu/search/q=year%3A{year}%20author%3A%22%5E{author}%22&sort=date%20desc%2C%20bibcode%20desc&p_=0".format(year=year, author=author)
        # The following url contains a filter: Collection:+astronomy
        url = "'https://ui.adsabs.harvard.edu/search/filter_database_fq_database=AND&filter_database_fq_database=database%3A%22astronomy%22&fq=%7B!type%3Daqp%20v%3D%24fq_database%7D&fq_database=(database%3A%22astronomy%22)&p_=0&q=year%3A{year}%20author%3A%22%5E{author}%22&sort=date%20desc%2C%20bibcode%20desc'".format(year=year, author=author)
        print("opening " + url)
        if not parse.nob:
            os.system("open " + url)


def main_v3():
    parser, parse = parse_args_v3()
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(2)
    if parse.kind == "t":
        args = {"year": "1955", "jour": "ApJ", "vol": "121", "page": "161"}
        print("Parsed input:", args)
        url = geturl(args)
        print("opening " + url)
        os.system("open " + url)
        print("This should open a brower tab and direct to Salpeter's "
                "1955 paper on ADS")
    if parse.kind == "a":
        sys.exit(os.system("ads2bibdesk " + parse.a))
        return
    if parse.kind == "r":
        args = {"year": parse.params[0], "jour": parse.params[1], "vol":
            parse.params[2], "page": parse.params[3]}
        args = clean_args(args)         # dict
        args = validate_ads(**args)     # dict
        print("Parsed input:", args)
        url = geturl(args)
        print("opening " + url)
        os.system("open " + url)
    if parse.kind == "ay":
        theauthor = parse.params[0]
        if theauthor[-2:].isdigit():
            if theauthor[-4:].isdigit():
                author = theauthor[:-4]
                year = theauthor[-4:]
            else:
                author = theauthor[:-2]
                year = int(theauthor[-2:])
                year = 1900 + year if year >= 50 else 2000 + year
        else:
            author = theauthor[0]
            year = parse.params[1]
        print("Parsed input: author = {}, year = {}".format(author, year))
        # url = "https://ui.adsabs.harvard.edu/search/q=year%3A{year}%20author%3A%22%5E{author}%22&sort=date%20desc%2C%20bibcode%20desc&p_=0".format(year=year, author=author)
        # The following url contains a filter: Collection:+astronomy
        url = "'https://ui.adsabs.harvard.edu/search/filter_database_fq_database=AND&filter_database_fq_database=database%3A%22astronomy%22&fq=%7B!type%3Daqp%20v%3D%24fq_database%7D&fq_database=(database%3A%22astronomy%22)&p_=0&q=year%3A{year}%20author%3A%22%5E{author}%22&sort={thesort}%20desc%2C%20bibcode%20desc'".format(year=year, author=author, thesort=SORT)
        print("opening " + url)
        os.system("open " + url)

def main():
    print("main")

if __name__ == '__main__':
    # print("Hello, world!")
    # main_v2()
    main_v3()
