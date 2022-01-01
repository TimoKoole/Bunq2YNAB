import pandas as pd

EXPORT_COLUMNS = ["Date", "Payee", "Category", "Memo", "Outflow", "Inflow"]


def convert_date(date):
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    return day + '/' + month + '/' + year


class Converter:
    def __init__(self, input_file: str = None, data=None):
        if data is None:
            self.input_data = pd.read_csv(input_file, parse_dates=[0], decimal='.', thousands=",")
        else:
            self.input_data = data
        print(str(self.input_data.to_dict()).replace(" nan", " float('nan')"))
        self.output_data = pd.DataFrame(
            index=self.input_data.index, columns=EXPORT_COLUMNS, data=None)

    def convert(self):
        self.output_data['Date'] = self.input_data['Date'].apply(convert_date)
        self.output_data['Payee'] = self.input_data['Name']
        self.output_data['Memo'] = self.input_data['Description']
        self.output_data['Outflow'] = self.input_data[self.input_data['Amount'].astype(float) < 0]['Amount'].astype(
            float) * -1
        self.output_data['Inflow'] = self.input_data[self.input_data['Amount'] >= 0]['Amount']
        self.output_data.fillna('', inplace=True)

    def write_output_file(self, output_file):
        self.output_data.to_csv(output_file)
