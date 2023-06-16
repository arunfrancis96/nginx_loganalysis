import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Nginx Log Analysis", #setting the configuration of the webpage
                   page_icon="🐧",
                   layout='wide'
)
#creating the containers
head = st.container() 
logdata = st.container()
table = st.container()
features = st.container()


with head:
    
    st.title("Nginx log analysis with python") #Gives the name for the title
    

with logdata:
    log_file = pd.read_csv("ngnix_log.csv") #uploading our log data

    ipaddress_dist = pd.DataFrame(log_file['IP_Address'].value_counts()) #shows how many time an ip address is represent in the log

with table:
    st.subheader("Log Table")

    st.sidebar.header("Please Filter here")
    st.sidebar.subheader("1.Informational responses (100-199)") #adding the sidebar for filtering
    st.sidebar.subheader("2.Successful responses (200-299)")
    st.sidebar.subheader("3.Redirection messages (300-399)")
    st.sidebar.subheader("4.Client error responses (400-499)")
    st.sidebar.subheader("5.Server error responses (500-599)")
    # These are yet to be updated
    #IP_Address = st.sidebar.multiselect( 
#        "Select the IP Address:",
        #options=log_file["IP_Address"].unique(),
        ##default=log_file["IP_Address"].unique()
    #)
    #Request_type = st.sidebar.multiselect(
#        "Select the Request type",
        #options=log_file["Request_type"].unique(),
        #default=log_file["Request_type"].unique()
    #)
    Response_code = st.sidebar.multiselect( #This filters out the rows that contain a specific response code
        "Select the Response code",
        options=log_file["Response_code"].unique(),
        default=log_file["Response_code"].unique()
    )

    df_selection = log_file.query(
         "Response_code == @Response_code" 
    )
    #Creating a table using plotly
    fig = go.Figure(data=go.Table( 
        columnwidth=[3,5,3,9,3,3,3,3.7],
        header=dict(values=list(df_selection[['IP_Address','Timestamp','Request_type','Access','Response_code','Bytes_sent','Operating_system','Browser']])
                ,align='center',font=dict(size=12),fill_color='#306EFF'),
     cells=dict(values=[df_selection.IP_Address, df_selection.Timestamp, df_selection.Request_type,df_selection.Access, df_selection.Response_code, df_selection.Bytes_sent, df_selection.Operating_system, df_selection.Browser], 
                fill_color='#000000', align='left', font=dict(size=16))))

    fig.update_layout(
        margin=dict(l=2,r=2,b=5, t=5) #updates the margin
        )
    fig.update_layout(  #updates the position
        height=500,
        width=1200
    )

    st.write(fig) #displays the table

with features:
    #creating a pie chart
    st.subheader("IP Address activies:") 
    pie_col = st.empty()

    ipaddress_dist = ipaddress_dist.reset_index() #uses the function that is defined at the log_data header
    ipaddress_dist.columns = ['IP_Address','count']

    fig = px.pie(ipaddress_dist, values= 'count', names='IP_Address')
    
    #Customizing the font size
    fig.update_layout(
    showlegend=True,
    legend=dict(
        font=dict(
            size=18
        )
    ),  
    font=dict(
        size=18  
    ))
    #Displaying the pie chart
    pie_col.write(fig)


    

    

   