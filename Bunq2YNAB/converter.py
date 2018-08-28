import sys
import os
import pandas as pd


class Converter():
    def __init__(self, inputfile):
        self.inputdata = pd.read_csv(inputfile, parse_dates=[0])
        self.outputdata = pd.DataFrame(
            index=self.inputdata.index, columns=EXPORT_COLUMNS, data=None)

    def convert(self):
        self.outputdata['Date'] = self.inputdata['Datum']
        self.outputdata['Payee'] = self.inputdata['Name']
        self.outputdata['Memo'] = self.inputdata['Description']
        self.outputdata['Outflow'] = self.inputdata[self.inputdata['Amount'] < 0]['Amount'] * -1
        self.outputdata['Inflow'] = self.inputdata[self.inputdata['Amount'] >= 0]['Amount']
        self.outputdata.fillna('', inplace=True)

    def write_outputfile(self, outputfolder, outputfile):
        os.makedirs(outputfolder, exist_ok=True)
        self.outputdata.to_csv(os.path.join(outputfolder, outputfile))


if __name__ == '__main__':
    converter = Converter('2018-08-28_19-51-52_bunq-statement.csv')
    converter.convert()
    converter.write_outputfile( os.path.dirname(sys.argv[0]),'bunq.csv' )
