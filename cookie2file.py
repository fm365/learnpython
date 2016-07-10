import urllib2
import cookielib

def HandleCookie():
    filename = 'FileCookieJar.txt'
    url = 'http://cn.bing.com'
    FileCookieJar = cookielib.LWPCookieJar(filename)
    FileCookieJar.save()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(FileCookieJar))
    opener.open(url)
    FileCookieJar.save()
    
    print open(filename).read()

if __name__ == "__main__":
    HandleCookie()
