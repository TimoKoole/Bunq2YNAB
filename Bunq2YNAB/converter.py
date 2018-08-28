import sys
import os
import pandas as pd

EXPORT_COLUMNS = ["Date", "Payee", "Category", "Memo", "Outflow", "Inflow"]

def convert_date(date):
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    return day + '/' + month + '/' + year


class Converter():
    def __init__(self, inputfile):
        self.inputdata = pd.read_csv(inputfile, parse_dates=[0])
        self.outputdata = pd.DataFrame(
            index=self.inputdata.index, columns=EXPORT_COLUMNS, data=None)

    def convert(self):
        self.outputdata['Date'] = self.inputdata['Date'].apply(convert_date)
        self.outputdata['Payee'] = self.inputdata['Name']
        self.outputdata['Memo'] = self.inputdata['Description']
        self.outputdata['Outflow'] = self.inputdata[self.inputdata['Amount'] < 0]['Amount'] * -1
        self.outputdata['Inflow'] = self.inputdata[self.inputdata['Amount'] >= 0]['Amount']
        self.outputdata.fillna('', inplace=True)

    def write_outputfile(self, outputfolder, outputfile):
        os.makedirs(outputfolder, exist_ok=True)
        self.outputdata.to_csv(os.path.join(outputfolder, outputfile))


if __name__ == '__main__':
    converter = Converter(os.path.dirname(sys.argv[0]) + '\\transactions.csv')
    converter.convert()
    converter.write_outputfile( os.path.dirname(sys.argv[0]),'bunq.csv' )
