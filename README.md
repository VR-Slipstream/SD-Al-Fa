# SD-Al-Fa
Tool to identify web-domains which are alive and generate favicon hash

Required modules:
subprocess , requests, mmh3, codecs, argparse
install them individually using pip

or

$ pip install -r requirements.txt


Usage:
$ python3 sd-al-fa.py -d <domain.tld> -s <sub_domains.txt> -status <sub_domain_status.txt> -fh <sub_domain_favicon_hash.txt>

It'll create 3 files
1. subdomains
2. filtered subdomains with status code
3. favicon hashes

To avoid confusion, create a new directory and execute the script
