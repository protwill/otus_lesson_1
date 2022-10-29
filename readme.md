# Description
Link scraper for OTUS Python course, lesson 1.
# Usage:
`parser.py [OPTIONS] URL`\
where `URL` is initial link to start from.
## Options:
`--file` (TEXT) - Path to output file. If undefined then output to the screen.\
`--recursion_depth` (INTEGER) - Depth of recursion for nested links. Default is 1.\
`--timeout` INTEGER - Connection timeout in seconds for get URL method. Default is 1.\
`--limit` INTEGER - Limit link per page, if 0 then no limit. Default is 0.\
`--help` - Show help message and exit.
# Example
`python parser.py --file './out.txt' --recursion_depth 2 --limit 3 'https://example.org/'`
Scrape urls in site "https://example.org/" into "out.txt" file in current dir, with recursion depth = 2 for nested links and limit for 3 links per page.