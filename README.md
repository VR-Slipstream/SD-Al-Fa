# SD-Al-Fa
Tool to identify sub-domains which are alive and generate favicon hash

Requirements:
subprocess, requests, mmh3, codecs, argparse

subfinder:
$ sudo apt install subfinder

or

$ go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest


$ pip install -r requirements.txt


Usage:
$ python3 sd-al-fa.py -d <domain.tld> -s <sub_domains.txt> -status <sub_domain_status.txt> -fh <sub_domain_favicon_hash.txt>

It'll create 3 files
1. subdomains
2. filtered subdomains with status code
3. favicon hashes

To avoid confusion, create a new directory and execute the script
