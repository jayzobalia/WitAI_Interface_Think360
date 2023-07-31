def Avg_LoanType(resp, df):
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
    else:
        text = "Sorry I couldnt find an answer. Please proivde a different Question."

    return text

