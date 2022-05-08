import pandas as pd
import plotly.express as px

df = pd.read_csv('viz_data.csv')

df = df[(df['Topic'] == "Mental Health") & 
    (df['Question'].str.contains("Recent mentally unhealthy days among adults aged >= 18 years")) & 
    (df['DataValueType'] == "Age-adjusted Mean")]

df = df[df['DataValue'] != 0]

df = df.rename(columns = {'YearEnd': 'Year', 'DataValue': 'Value', 'LocationAbbr': 'State'})

fig = px.choropleth(df,
                    locations='State', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='Value',
                    animation_frame='Year'
                    )

fig.update_layout(
      title_text = 'Average Number of Mentally Unhealthy Days in the United States <br><sup> Age-adjusted average for Adults (individuals 18 and older) from 2011 to 2019. </sup>',
      title_font_family="Times New Roman",
      title_font_size = 22,
      title_font_color="black", 
      title_x=0.45,
      template = "simple_white",
      font_family="Times New Roman"
    )

fig.write_html('choropleth.html')

df = df.sort_values(by = ['Year', 'Value'])

df = df[(df['State'] == 'WV') | (df['State'] == 'AL') | (df['State'] == 'LA') | (df['State'] == 'AR') | (df['State'] == 'KY')]


fig2 = px.line(df, x="Year", y="Value", color = "State")

fig2.update_layout(
      title_text = 'Trends of Average Number of Mentally Unhealthy Days in the United States<br>' +
    '<sup> Focusing on the Five States with the Highest Average Number of Mentally Unhealthy Days in 2019.</sup>',
      title_font_family="Times New Roman",
      title_font_size = 22,
      title_font_color="black", 
      title_x=0.45,
      template = "simple_white",
      font_family="Times New Roman"
    )

fig2.update_yaxes(title_text='Age-Adjusted Average Number of Mentally Unhealthy Days')

fig2.write_html('trends.html')