from datetime import datetime
from wit import Wit

client = Wit("DFYDQOB2CFXCQ4GUPIZETRHOR2NXLS2E")


def n_time(resp, df):
    df['Application Date'] = df['Application Date'].apply(lambda x: datetime.strptime(x, '%d-%m-%Y'))

    if (resp['entities']["Columns:Columns"])[0]['value'] == "cibil score":
        column_value = "Cibil Score"

    elif (resp['entities']["Columns:Columns"])[0]['value'] == "loan amount":
        column_value = "Loan Amount"

    elif (resp['entities']["Columns:Columns"])[0]['value'] == "interest rate":
        column_value = "Interest Rate"

    elif (resp['entities']["Columns:Columns"])[0]['value'] == "EMI amount":
        column_value = "EMI Amount"

    elif (resp['entities']["Columns:Columns"])[0]['value'] == "credit limit":
        column_value = "Credit Limit"

    elif (resp['entities']["Columns:Columns"])[0]['value'] == "current balance":
        column_value = "Current Balance"

    elif (resp['entities']["Columns:Columns"])[0]['value'] == "high credit amount":
        column_value = "High Credit Amount"



    start_date = ((resp['entities']["wit$datetime:datetime"])[0]['from'])['value']
    end_date = ((resp['entities']["wit$datetime:datetime"])[0]['to'])['value']
    start_date = datetime.strptime(start_date[0:10], '%Y-%m-%d')
    end_date = datetime.strptime(end_date[0:10], "%Y-%m-%d")

    filtered_df = df[(df['Application Date'] >= start_date) & (df['Application Date'] <= end_date)]

    text = "hello world"

    if (resp['entities']["Functions:Functions"])[0]["value"] == 'minimum':
        text = filtered_df[column_value].min()

    elif (resp['entities']["Functions:Functions"])[0]["value"] == 'maximum':
        text = filtered_df[column_value].max()

    elif (resp['entities']["Functions:Functions"])[0]["value"] == 'mean':
        text = filtered_df[column_value].mean()

    return text


