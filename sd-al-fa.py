import subprocess as sp, requests, mmh3, codecs, argparse

parser = argparse.ArgumentParser(description="Get Subdomains, subdomains which are alive and their favicon Hashes")
parser.add_argument("-d", type=str, help="Resolve DNS", required=True)
parser.add_argument("-s", type=str, help="Output subdomains", required=True)
parser.add_argument("-status", type=str, help="Output with status codes", required=True)
parser.add_argument("-fh", type=str, help="Output with Favicon Hashes", required=True)
b = parser.parse_args()

if b.d:
    subs = sp.getoutput("subfinder -d " + b.d + " -silent")
    print(subs)
if b.s:
    f = open(b.s, "w")
    f.write(subs)
    f.close()
if b.status:
    f = open(b.s, "r")
    subdomains = f.readlines()
    f.close()   
    f = open(b.status, "a")
    hd = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    for subdomain in subdomains:
        try:
            h = "https://" + subdomain.strip()
            h_status_code = requests.get(h, headers=hd, timeout=10).status_code
            g = "http://" + subdomain.strip()
            g_status_code = requests.get(g, headers=hd, timeout=10).status_code
            print(h, "[" + h_status_code + "]")
            print(g, "[" + g_status_code + "]")
            if int(h_status_code) == 200:
                f.write(h + " " + "[200]\n")
            elif int(g_status_code) == 200:
                f.write(g + " " + "[200]\n")
        except:
            pass
    f.close()

if b.fh:
    f = open(b.status, "r")
    web_alive = f.readlines()
    f.close()

    for fav in web_alive:
        fav_url = fav.split()[0].strip() + "/favicon.ico"

        with open(b.fh, "a") as ff:
            favicon = codecs.encode(requests.get(d).content, "base64")
            hash = mmh3.hash(favicon)
            print(fav_url, "[" + hash + "]")
            ff.write(d + " [" + str(hash) + "]\n")
        ff.close()
