

class pageCheckError(Exception):
    def __init__ (self, current_url, errors):
        self.current_url = current_url
        self.errors = errors
        super().__init__(f"Page check Error in url: {current_url}")

