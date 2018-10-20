!#/usr/bin/pyhon
from bs4 import BeautifulSoup
import urllib, urllib2, os
from progress.bar import Bar
totalsize = 0
def SaveFile(link, numstr):
    global totalsize
    try:
        site = urllib2.urlopen(link)
        filename = link.split('/')[-1]
        if site.code == 200:
            f = open('Files\\' + filename,'wb')
            file_info = site.info()
            size = int(file_info["Content-Length"])
            if len(str(size)) < 7:
                file_size = str("%.1f" % float(int(size) * 0.001)) + 'KB'
            elif len(str(size)) > 6:
                file_size = str("%.1f" % (int(size) * 0.000001)) + 'MB'
            else:
                pass
            original_size = size
            totalsize += size
            while size > 0:
                f.write(site.read(1000))
                size -= 1000
            f.close()
            validfile = os.path.getsize('Files\\' + filename)
            if validfile == 0:
                os.remove('Files\\' + filename)
                print '>> Error: File is empty'
            elif validfile == original_size:
                print '>> [%s] File %s saved successfully (Size: %s)' % (numstr, filename, file_size)
            else:
                print '>> Error: something wrong'
    except:
        pass


URL = 'https://www.digitalwhisper.co.il/Issues/'
site = urllib.urlopen(URL)
parse =  BeautifulSoup(site.read(), features='html.parser')
find_href = parse.findAll('a')
all_links = []
pdf_links = []
for i in find_href:
    link = i.encode('utf-8').split('"')[1]
    if '#' not in link:
        if 'http' in link and 'digitalwhisper.' in link:
            all_links.append(link)
        elif '../../' in link:
            link = link.strip('../../')
            new_URL = URL.split('/')
            del new_URL[-2]
            new_URL = '/'.join(new_URL)
            all_links.append(new_URL + link)

bar = Bar('Processing', max=len(all_links))
num = 1
for link in all_links:
    print '>> Opening url:',link, '(' + str(num) + '/' + str(len(all_links)) + ')'
    num += 1
    bar.next()
    try:
        site = urllib.urlopen(link)
        parse = BeautifulSoup(site.read(), features='html.parser')
        find_href = parse.findAll('a')
        for i in find_href:
            href = i.encode('utf-8').split('"')[1]
            if '.pdf' in href:
                if '../../' in href:
                    href = href.strip('../../')
                    new_link = link.split('/')
                    del new_link[-1]
                    new_link = '/'.join(new_link) + '/' + href
                    # SaveFile(new_link)
                    pdf_links.append(new_link)
                elif 'http' not in href:
                    pdf_links.append(link + href)
                else:
                    pdf_links.append(href)
    except:
        pass
bar.finish()

try:
    os.stat('Files')
except:
    os.mkdir('Files')

num = 0
lenlinks = len(list(set(pdf_links)))
f = open('links.txt', 'w')
print '\nStating to download files...\n'
for linkfile in list(set(pdf_links)):
    num += 1
    numstr = str(num) + '/' + str(lenlinks)
    f.write(linkfile + '\n')
    SaveFile(linkfile, numstr)
f.close()
filesdir = os.getcwd() + '\\Files'
totalsize = str("%d" % (int(totalsize) * 0.000001)) + 'MB'
num = str(num)
print '>> Done\n%s files has been downloaded to %s (Total size: %s)' % (num, filesdir, totalsize)
