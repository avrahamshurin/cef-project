from cef_request_handler import CefRequestHandler
from request_to_df_parser import RequestToDfParser


class CefDataManager():
    def __init__(self):
        self.request_handler = CefRequestHandler()
        self.parser = RequestToDfParser()
    
    def get_data(self):
        # TODO check if method was called already today, and cache result 
        response = self.request_handler.make_request()
        return self.parser.get_df(response)
