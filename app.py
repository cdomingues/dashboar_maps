import streamlit as st
import pandas as pd
#from altair.vegalite.v4.api import Chart

APP_TITLE = 'Fraud and identity Theft Report'
APP_SUBTITLE = 'Source: Federal Trade Comission'

def display_fraud_facts(year, quarter, state_name, report, field_name, metric_title):


def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)

        

    #Carregando dados

    df = pd.read_csv('data/AxS-Fraud Box_Full Data_data.csv')

    year = 2022
    quarter = 1
    state_name = ''
    report_type = 'Other'
    field_name = 'State Fraud/Other Count'
    metric_title = f'#{report_type} of Reports'
    
    df = df[(df['Year'] == year) & (df['Quarter'] == quarter) & (df['Report Type'] == report_type)]
    if state_name:
        df = df[df['State Name'] == state_name]
    df.drop_duplicates(inplace=True)
    total = df[field_name].sum()
    st.metric(metric_title,'{:,}'.format(total))

    st.write(df.shape)
    st.write(df.head())
    st.write(df.columns)




if __name__ == "__main__":
    main()