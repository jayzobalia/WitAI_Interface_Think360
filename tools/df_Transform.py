def to_master_df(df,client, pd):
    column_names = df.columns.tolist()
    resp_list = []
    for i in column_names:
        try:
            resp = client.message(i)
            resp_list.append(resp['entities']['column_name:column_name'][0]['value'])
        except IndexError:
            pass

    columns = ['Applicant ID', 'Application Date', 'Age', 'Cibil Score', 'Loan Type', 'Loan Amount', 'Interest Rate', 'Date Open',
               'Date Close', 'EMI Amount', 'Credit Limit', 'Current Balance', 'dpd String', 'High Credit Amount', 'Postalcode']
    new_df = pd.DataFrame(columns=columns)

    for i in resp_list:
        if i == "Applicant ID":
            new_df["Applicant ID"] = df["applicant_id"]

        elif i == "Application Date":
            new_df["Application Date"] = df["application_date"]

        elif i == "Age":
            new_df["Age"] = df["age"]

        elif i == "Cibil Score":
            new_df["Cibil Score"] = df["cibil_score"]

        elif i == "Loan Type":
            new_df["Loan Type"] = df["loan_type"]

        elif i == "Loan Amount":
            new_df["Loan Amount"] = df["loan_amount"]

        elif i == "Intrest Rate":
            new_df["Interest Rate"] = df["interest_rate"]

        elif i == "Date Open":
            new_df["Date Open"] = df["date_open"]

        elif i == "Date Close":
            new_df["Date Close"] = df["date_close"]

        elif i == "EMI Amount":
            new_df["EMI Amount"] = df["emi_amount"]

        elif i == "Credit Limit":
            new_df["Credit Limit"] = df["credit_limit"]

        elif i == "Current Balance":
            new_df["Current Balance"] = df["current_balance"]

        elif i == "dpd String":
            new_df["dpd String"] = df["dpd_string"]

        elif i == "High Credit Amount":
            new_df["High Credit Amount"] = df["high_credit_amount"]

        elif i == "Postalcode":
            new_df["Postalcode"] = df["postalcode"]

    return new_df

