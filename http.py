class HttpRequest:

    def __init__(self, request: str):
        self.request = request
        parsed_request = request.split(" ")
        self.method = parsed_request[0]
        self.path = parsed_request[1].strip()

        print(self.path)

    @property
    def device(self):
        return self.path.split("/")[0]

    @property
    def state(self):
        return self.path.split("/")[1]