import mechanize

def callWithProxy(url, userAgent, proxyAddress):
    browser = mechanize.Browser()
    browser.addheaders = userAgent
    browser.set_proxies(proxyAddress)
    browser.set_handle_robots(False)
    page = browser.open(url)
    source_code = page.read()
    print source_code
    
def main():
    url = "http://whatsmyuseragent.org"
    hideMyAssProxy = {'http' : '169.159.132.30:8080'}
    userAgent = [('User-agent', 'Opera/9.26 (Windows NT 5.1; U; de))')]
    callWithProxy(url, userAgent, hideMyAssProxy)
    
if __name__ == "__main__":
    main() 
