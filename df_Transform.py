def to_master_df(df,client, pd):
    column_names = df.columns.tolist()
    resp_list = []
    for i in column_names:
        try:
            resp = client.message(i)
            resp_list.append((resp["intents"][0])["name"])
        except IndexError:
            pass

    print(resp_list)
    columns = ['Applicant ID', 'Application Date', 'Age', 'Cibil Score', 'Loan Type', 'Loan Amount', 'Interest Rate', 'Date Open',
               'Date Close', 'EMI Amount', 'Credit Limit', 'Current Balance', 'dpd String', 'High Credit Amount', 'Postalcode']
    new_df = pd.DataFrame(columns=columns)

    for i in resp_list:
        if i == "Application_ID":
            new_df["Applicant ID"] = df["applicant_id"]

        elif i == "Application_date":
            new_df["Application Date"] = df["application_date"]

        elif i == "age":
            new_df["Age"] = df["age"]

        elif i == "score":
            new_df["Cibil Score"] = df["cibil_score"]

        elif i == "loan_type":
            new_df["Loan Type"] = df["loan_type"]

        elif i == "Loan_Amount":
            new_df["Loan Amount"] = df["loan_amount"]

        elif i == "Intrest_Rate":
            new_df["Interest Rate"] = df["interest_rate"]

        elif i == "date_open":
            new_df["Date Open"] = df["date_open"]

        elif i == "date_close":
            new_df["Date Close"] = df["date_close"]

        elif i == "emi_amount":
            new_df["EMI Amount"] = df["emi_amount"]

        elif i == "credit_limit":
            new_df["Credit Limit"] = df["credit_limit"]

        elif i == "current_balance":
            new_df["Current Balance"] = df["current_balance"]

        elif i == "dpd_string":
            new_df["dpd String"] = df["dpd_string"]

        elif i == "high_credit_amount":
            new_df["High Credit Amount"] = df["high_credit_amount"]

        elif i == "postalcode":
            new_df["Postalcode"] = df["postalcode"]

    return new_df


