class BaseOAuth(object):

    def signup(self, access_token):
        raise NotImplementedError("Does Not Implemented")

    def login(self, access_token):
        raise NotImplementedError("Does Not Implemented")
