
class RedirectionError(Exception):
    def __init__ (self, current_url):
        self.current_url = current_url
        super().__init__(f"Redirection Error. current_url {current_url}")


class pageCheckError(Exception):
    def __init__ (self, current_url, errors):
        self.current_url = current_url
        self.errors = errors
        super().__init__(f"Page check Error in url: {current_url}")


class BrokenLinkError(Exception):
    def __init__(self, url, status_code, error_content):
        self.url = url
        self.status_code = status_code
       
        super().__init__(f"Broken link: {url}  (Status: {status_code})")