# ads_search

A simple NASA ADS query tool that works.

## Key Features

- Copy bibtex into clipboard or open the ads entry in browser. (Tested on macOS)
- Possibly the easiest workflow possible: copy a MNRAS/ApJ style reference, e.g. `1955, ApJ, 121, 161`, as the arguments of the `ads` command, and the bibtex entry will be copied into your clipboard.

## How to Use

To clone and use this application, you'll need [Git](https://git-scm.com) and Python installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/chongchonghe/ads_search.git

# Go into the repository
$ cd ads_search

# Install adssearch
$ make

# OR, alternatively,
$ pip install -e .

# Run the test
$ ads -t
```

Example use:

```bash
>>> ads 1955, ApJ, 121, 161
>>> ads 2002, A\&A, 382, 28
>>> ads 2002, 'A&A' 382, 28
>>> ads -w 1955, ApJ, 121, 161
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

MIT
