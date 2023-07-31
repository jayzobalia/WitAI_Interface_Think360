import pandas as pd
import streamlit as st
from wit import Wit
from tools import df_Transform, Average_LoanType, rolling_date

client = Wit("DFYDQOB2CFXCQ4GUPIZETRHOR2NXLS2E")
client2 = Wit("FI4PN574BAQDRINH2LTUOEC65R7WQCD7")


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
        df = df_Transform.to_master_df(df, client2, pd)
    elif check_xlsx(uploaded_file):
        df = pd.read_excel(uploaded_file)
        # df = df_Transform.to_master_df(df.to_csv())

    resp = client.message(input_text)

    if (resp["intents"][0])["name"] == 'AggregateCalculator_with_LoanType':
        text = Average_LoanType.Avg_LoanType(resp, df)

    elif (resp["intents"][0])["name"] == "TimeFrame":
        text = rolling_date.n_time(resp, df)



    st.text_area("Output", value=text)

prompts = "1. calculate the average of emi amount of applicants with personal loan\n2. Calculate the average cibil score of " \
          "applicants with home loans\n3. get me the " \
          "average intrrest rate with home loans "

st.text_area("Example Promots:", value=prompts)
df = pd.read_csv("DataSet/llm_sample_dataset.csv")


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
