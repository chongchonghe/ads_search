# ads_search

A simple NASA ADS query tool that works.

<!-- ## Key Features -->

<!-- - Copy bibtex into clipboard or open the ads entry in browser. (Tested on macOS) -->
<!-- - Possibly the easiest workflow possible: copy a MNRAS/ApJ style reference, e.g. `1955, ApJ, 121, 161`, as the arguments of the `ads` command, and the bibtex entry will be copied into your clipboard. -->

## Installation

Clone this repository and install it via `pip`:

To clone and use this application, you'll need [Git](https://git-scm.com) and Python installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/chongchonghe/ads_search.git

# Go into the repository
$ cd ads_search

# OR, alternatively,
$ pip install -e .

# Run a test
$ ads -t
```

## Usage

```bash
>>> ads
usage: ads [-h] [-b BIBLIOGRAPHY BIBLIOGRAPHY BIBLIOGRAPHY BIBLIOGRAPHY] [-ay AY [AY ...]] [-a ARTICLE_IDENTIFIER] [-nob] [-t]

A simple ads parser that works.

Can do one of the following:
1. Find the url of a paper on ADS witha given a ApJ/MNRAS style bibliography
2. Find the url of a paper on ADS witha given the author and year
3. Add a article to BibDesk given a article identifier

Author: Chong-Chong He (che1234@umd.edu)

Examples:
>>> ads -ay Salpeter55
>>> ads -ay Salpeter1955
>>> ads -ay Salpeter 1955
>>> ads -b 1955, ApJ, 121, 161
>>> ads -a 1955ApJ...121..161S

optional arguments:
  -h, --help            show this help message and exit
  -b BIBLIOGRAPHY BIBLIOGRAPHY BIBLIOGRAPHY BIBLIOGRAPHY
                        Open a browser tab and direct to an ADS page of the given article specified by a ApJ/MNRAS style bibliography. The tracing commas will be ignored. Replace '&' with '\&' in the journal name. e.g.
                        	ads -b 1955, ApJ, 121, 161
                        	ads -b 2002, A\&A, 382, 28
  -ay AY [AY ...]       Open a browser tab and direct to an ADS page of the given article specified by first author and year. Two-digit number are idendified as 19xx if bigger than 50 else as 20xx. e.g.
                        	ads -ay Salpeter 1955
                        	ads -ay Salpeter1955
                        	ads -ay Salpeter55.
  -a ARTICLE_IDENTIFIER
                        Add article to bibdesk. Accept bibcode/arxiv id/doi as the article_identifier. Equivalent to 'ads2bibdesk ARTICLE_IDENTIFIER'. e.g.
                        	ads -a 1955ApJ...121..161S
  -nob                  Toggle off 'open url in borwser'
  -t                    Run a test: 'ads -b 1955, ApJ, 121, 161'
```

## Credits

This software uses the following open source packages:

- [ads](https://pypi.org/project/ads/)
- [argparse](https://pypi.org/project/argparse/)

## Related

[ads2bibdesk](https://pypi.org/project/ads2bibdesk/) - A Python package that inspired this program. I couldn't make it work, so I wrote my own application as a simple and minimal alternative. 

## Author

Chong-Chong He ([che1234@umd.edu]())

## License

MITl

