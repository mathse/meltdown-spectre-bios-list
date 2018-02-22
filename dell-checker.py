import urllib2, os
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen('http://www.dell.com/support/article/de/de/debsdt1/sln308587/microprocessor-side-channel-vulnerabilities-cve-2017-5715-cve-2017-5753-cve-2017-5754-impact-on-dell-products?lang=en#Dell_Products_Affected').read()
soup = BeautifulSoup(page)
soup.prettify()
for row in soup.findAll('table')[1].findAll('tbody')[0].findAll('tr'):
    name = row.findAll('td')[0].text
    new_version = row.findAll('td')[1].text
    try:
        # t =
        # print name
        old_version = os.popen("grep '%s' README.md" % name).read().split(" | ")[1].replace(" ","").replace("\n","")
        if old_version != new_version and new_version != "In Process":
            # print old_version
            print "%s \t %s -> %s" % (name,old_version,new_version)
    except:
        print "%s is missing" % name
