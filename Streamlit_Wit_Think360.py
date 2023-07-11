import pandas as pd
import streamlit as st
from wit import Wit
import df_Transform

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


st.title("Welcome Jay!")

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
        df = df_Transform.to_master_df(df, client, pd)
    elif check_xlsx(uploaded_file):
        df = pd.read_excel(uploaded_file)

    resp = client.message(input_text)
    hl_vals = []
    al_vals = []
    pl_vals = []

    for i in range(len(df["Loan Type"])):
        if df["Loan Type"][i] == "Home Loan":
            hl_vals.append(i)
        elif df["Loan Type"][i] == "Auto Loan":
            al_vals.append(i)
        elif df["Loan Type"][i] == "Personal Loan":
            pl_vals.append(i)

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
        text = "The average " + column_value + " of applicants that have taken " + \
               resp['entities']["loan_type:loan_type"][0]['value'] + " is: " + str(hl_text)
    elif pl_text > 0:
        text = "The average " + column_value + " of applicants that have taken " + \
               resp['entities']["loan_type:loan_type"][0]['value'] + " is: " + str(pl_text)
    elif al_text > 0:
        text = "The average " + column_value + " of applicants that have taken " + \
               resp['entities']["loan_type:loan_type"][0]['value'] + " is: " + str(al_text)

    st.text_area("Output", value=text)

prompts = "1. calculate the average of emi amount of applicants with personal loan\n2. Calculate the average cibil score of " \
          "applicants with home loans\n3. get me the " \
          "average intrrest rate with home loans "


st.text_area("Example Promots:", value=prompts)
df = pd.read_csv("llm_sample_dataset.csv")

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
