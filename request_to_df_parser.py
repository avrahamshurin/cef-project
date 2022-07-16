from bs4 import BeautifulSoup
import pandas as pd
from reocrd_date import record_date


class RequestToDfParser():
    def __init__(self):
        pass

    # @record_date
    def get_df(self, response):
        table = self.__get_table(response)
        column_names = [item.text for item in table.find_all('th')]
        data_frame = pd.DataFrame(columns=column_names)

        for i, row in enumerate(table.find_all('tr')[1:]):
            data_frame.loc[i] = [val.text for val in row.find_all('td')]
        
        return data_frame

    def __get_table(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        return soup.find('table', class_='table')