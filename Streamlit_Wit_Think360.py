import pandas as pd
import streamlit as st
import string, csv
from wit import Wit

client = Wit("DFYDQOB2CFXCQ4GUPIZETRHOR2NXLS2E")


def check_csv(file):
    if uploaded_file:
        str = uploaded_file.name[-4:]
        if str == ".csv":
            return True
        else:
            return False


def check_xlsx(file):
    if uploaded_file:
        str = uploaded_file.name[-5:]
        if str == ".xlsx":
            return True
        else:
            return False


def check_pdf(file):
    if uploaded_file:
        str = uploaded_file.name[-4:]
        if str == ".pdf":
            return True
        else:
            return False


st.title("Welcome!")

col1, col2 = st.columns(2)

with col1:
    st.header("Input Prompt")
    input_text = st.text_input("You: ", "", key="input")

with col2:
    st.header("Input File")
    uploaded_file = st.file_uploader("Choose a file")

if input_text and uploaded_file:
    if check_csv(uploaded_file):
        df = pd.read_csv(uploaded_file)
    elif check_xlsx(uploaded_file):
        df = pd.read_excel(uploaded_file)

    resp = client.message(input_text)
    hl_vals = []
    al_vals = []
    pl_vals = []

    for i in range(len(df["loan_type"])):
        if df["loan_type"][i] == "Home Loan":
            hl_vals.append(i)
        elif df["loan_type"][i] == "Auto Loan":
            al_vals.append(i)
        elif df["loan_type"][i] == "Personal Loan":
            pl_vals.append(i)

    if (resp['entities']["Columns:Columns"])[0]['value'] == "cibil score":
        column_value = "cibil_score"

    elif (resp['entities']["Columns:Columns"])[0]['value'] == "loan amount":
        column_value = "loan_amount"

    elif (resp['entities']["Columns:Columns"])[0]['value'] == "interest rate":
        column_value = "interest_rate"

    elif (resp['entities']["Columns:Columns"])[0]['value'] == "EMI amount":
        column_value = "emi_amount"

    elif (resp['entities']["Columns:Columns"])[0]['value'] == "credit limit":
        column_value = "credit_limit"

    elif (resp['entities']["Columns:Columns"])[0]['value'] == "current balance":
        column_value = "current_balance"

    elif (resp['entities']["Columns:Columns"])[0]['value'] == "high credit amount":
        column_value = "high_credit_amount"

    sum_hl = 0
    sum_al = 0
    sum_pl = 0

    if (resp["intents"][0])["name"] == 'AggregateCalculator_with_LoanType':
        if resp['entities']["loan_type:loan_type"][0]['value'] == "Home loan":
            for i in hl_vals:
                sum_hl = sum_hl + df[column_value][i]

        if resp['entities']["loan_type:loan_type"][0]['value'] == "Auto loan":
            for i in al_vals:
                sum_al = sum_al + df[column_value][i]

        if resp['entities']["loan_type:loan_type"][0]['value'] == "Personal loan":
            for i in pl_vals:
                sum_pl = sum_pl + df[column_value][i]

    hl_text = sum_hl / len(hl_vals)
    pl_text = sum_pl / len(pl_vals)
    al_text = sum_al / len(al_vals)

    if hl_text > 0:
        text = "The average " + column_value + " of applicants that have taken "+resp['entities']["loan_type:loan_type"][0]['value'] + " is: " + str(hl_text)
    elif pl_text > 0:
        text = "The average " + column_value + " of applicants that have taken "+resp['entities']["loan_type:loan_type"][0]['value'] + " is: " + str(pl_text)
    elif al_text > 0:
        text = "The average " + column_value + " of applicants that have taken "+resp['entities']["loan_type:loan_type"][0]['value'] + " is: " + str(al_text)

    st.text_area("Output", value=text)
