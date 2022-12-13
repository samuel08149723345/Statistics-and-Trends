import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

indicator = pd.read_csv("Indicator API.csv")
print(indicator)

indicator.columns

df_ind = indicator.drop(columns=['Unnamed: 4'])
print(df_ind)

country = pd.read_csv("Country API.csv")
print(country)

country.columns

df_country = country.drop(columns=['Unnamed: 5'])
print(df_country)

df_country.isna().sum()

#Merging the Country and Indicators Dataframe as One single Dataframe
#Merging is done using Concat
all_api = pd.concat([df_country,df_ind], ignore_index=True)
print(all_api)

all_api.columns

df_all_api = all_api.drop(columns=['INDICATOR_CODE','INDICATOR_NAME','SOURCE_NOTE','SOURCE_ORGANIZATION'])
print(df_all_api)

#Structural shape of DataFrame
df_all_api.shape


#Filling all NaN data with Zero's
fill = df_all_api[["IncomeGroup", "Region", "TableName"]]
fill = df_all_api.fillna(0)
print(fill)

groups = df_all_api.groupby(['IncomeGroup'])['Region','TableName'].sum()
groups = groups.reset_index()
print(groups)

groups.describe()

#Total regions under each incomeGroup
IncomeGroup = df_all_api['IncomeGroup'].value_counts()
print(IncomeGroup)

#Here we get all the countries for each Global Region
Region = df_all_api['Region'].value_counts()
print(Region)

#All the tablename identifier
TableName = df_all_api['TableName'].value_counts()
print(TableName)
#Here we print all the Regions for each IncomeGroups
#Regions under the High Income Group
HighIncome = df_all_api.loc[df_all_api["IncomeGroup"] == "High income", "Region"].value_counts()
print(HighIncome)

#Regions under the low Income Group
LowIncome = df_all_api.loc[df_all_api["IncomeGroup"] == "Low income", "Region"].value_counts()
print(LowIncome)

#Regions under the Upper middle Income Group
UpperIncome = df_all_api.loc[df_all_api["IncomeGroup"] == "Upper middle income", "Region"].value_counts()
print(UpperIncome)

#Regions under the lowe middle Income Group
LowerMid = df_all_api.loc[df_all_api["IncomeGroup"] == "Lower middle income", "Region"].value_counts()
print(LowerMid)


#No 1 PIE CHART
Groups = [80,54,54,49,28]
label = ['High income','Lower middle income',
        'Upper middle income ', 'Low income','Missing Data']
explodes = [0.1,0,0,0,0.3]
title = ('Income groups')

    
def create_pie_chart(Groups,explodes,label):
    """
    Parameters
    ----------
    Groups : TYPE
        DESCRIPTION. Total countries that falls under each Income Groups
    explodes : TYPE
        DESCRIPTION. Shows area of focus in Pie-chart
    label : TYPE
        DESCRIPTION. The IncomeGroup

    Returns
    -------
    None.

    """
    plt.figure(dpi=70)
    plt.pie(Groups,labels=label, explode=explodes,autopct='%.2f%%', shadow=True)
    plt.title('INCOME GDP PERCENTAGE %')
    plt.savefig("GDP PERCENTAGE.png")
    plt.legend(bbox_to_anchor=(1.02,1),loc='lower left',borderaxespad=0)
    plt.savefig("pie_chart.png")
    plt.show()
create_pie_chart(Groups,explodes,label)


#Here we take a look into the continents in all income countries
#Also we get the value each region projects its GDP
    
y_axis = ('Europe & Central Asia ', 'Sub-Saharan Africa',
          'Latin America & Caribbean', 'East Asia & Pacific',
        'Middle East & North Africa','South Asia','North America','missing value')
x_axis = (58,48,42,37,21,8,3,48)
x_label = "Regions"
y_label = "GDP VALUES"
title = "GDP REGIONS "

def create_bar_chart(x_axis,y_axis,title,x_label, y_label,xticks):
    """
    Parameters
    ----------
    x_axis : TYPE
        DESCRIPTION. Total countries in each region
    y_axis : TYPE
        DESCRIPTION. All regions that makes up IncomeGroup
    title : TYPE
        DESCRIPTION. shows the impact of GDP in all areas
    x_label : TYPE
        DESCRIPTION. Allocating the plots for Regions
    y_label : TYPE
        DESCRIPTION. How much in (counts) GDP generated
    xticks : TYPE
        DESCRIPTION. Gives Positioning

    Returns
    -------
    None.

    """
#Bar char plotting
    plt.figure(dpi = 70)
    plt.bar(x_axis,y_axis,color=['red','orange','yellow','green','blue','indigo','violet','grey'])
#plt.bar(x_coords,Gain,tick_label=continent_group,)
    plt.xticks(rotation=90) #rotates text for x-axis labels 
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig("bar_chart.png")
    plt.show()
create_bar_chart(y_axis, x_axis, title,x_label,y_label,xticks=90)

# correlation score - Done
df_all_api['IncomeGroup']=df_all_api['IncomeGroup']
df_all_api['Region']=df_all_api['Region']
corr_1 = df_all_api.corr()
df_all_api['IncomeGroup']=df_all_api['IncomeGroup']
df_all_api['TableName']=df_all_api['TableName']
corr_2 = df_all_api.corr()

print(df_all_api.corr())


#HEAT MAP PLOTTING (Plot Our table) 
corr_score = [1.00, 0.429, -0.022, 0.429, 1.00, -0.023, -0.022, -0.023, 1.00]# correlation score
A = ['IncomeGroup' ,'IncomeGroup' ,'IncomeGroup', 'Region','Region', 'Region','TableName','TableName', 'TableName']
B = ['IncomeGroup' ,'Region' ,'TableName', 'IncomeGroup' ,'Region' ,'TableName', 'IncomeGroup' ,'Region' ,'TableName']
df = pd.DataFrame({'A': A,
                   'B': B,'corrrelation_score': corr_score})


#Plotting a heatmap
df_map = df.pivot_table(values='corrrelation_score',index='A',columns='B')
plt.figure()
plt.imshow(df_map,cmap = 'autumn')
plt.colorbar()
plt.ylabel('Section A')
plt.xlabel('Section B')
plt.title("GDP CORRELATION HEATMAP")
plt.show()



