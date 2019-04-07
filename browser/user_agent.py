import mechanize

def callWithUserAgent(url, userAgent):
    browser = mechanize.Browser()
    browser.addheaders = userAgent
    page = browser.open(url)
    source_code = page.read()
    print source_code   
    
def main():
    url = "http://whatsmyuseragent.org"
    userAgent = [('User-agent', 'Opera/9.26 (Windows NT 5.1; U; de))')]
    callWithUserAgent(url, userAgent)
    
if __name__=="__main__":
    main()