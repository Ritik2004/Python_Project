import pandas as pd
import datetime
import smtplib


GMAIL_ID = ""
GMAIL_PSWD = ""

def sendEmail(to, sub, msg):
    print(f"Email to {to} with subject {sub}")
    exit()

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)

    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()


if __name__ == "__main__":

    # this is used to read the excel sheet
    sendEmail(GMAIL_ID, "subject", "test message")
    exit()
    df = pd.read_excel("data.xlsx")
    # in today we are getting time in date,month and year
    # we can extract accordingly
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")

    writeInd = []
    for ind, item in df.iterrows():
        # print(ind, item['Name'])
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)

        # the second condition after and makes sure that mail is not send again and agian.
        # If we send in one year it mark that year

        if (today == bday) and yearNow not in str(item['Year']):
             sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
             writeInd.append(ind)

    # print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ',' + str(yearNow)

    # print(df)
    df.to_excel('data.xlsx', index=False)
