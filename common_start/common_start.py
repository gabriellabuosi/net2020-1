#!/usr/bin/env python
# coding: utf-8

# # This is an initial script to start playing with the data

# In[3]:


import pandas as pd 
import numpy as np 

import statsmodels
import statsmodels.api as sm
import scipy.stats as stats

import matplotlib.pyplot as plt

# import the csv file with all the comments and post togheter
# CHANGE THE PATH to you csv file
comDB = pd.read_csv(r"/home/salvo/Desktop/net2020/database/com_liwc.csv", sep='\t', engine='python')

# import the csv file with JUST the politicians post
postDB = pd.read_csv(r"/home/salvo/Desktop/net2020/database/postDB.csv", engine='python')


print (comDB)


# In[4]:


# general info ON COMMENT db
print('## Each row in the db is a comment, the information about the post that generate that comment are in the columns')
print('Number of colums in comDB : ', len(comDB.columns))
print('Number of rows in comDB : ', len(comDB.index))
print('')

# general info ON POST ONLY db
print('## Each row is a posts/tweets made by the politicians, this DB do not contain comments')
print('Number of colums in postDB : ', len(postDB.columns))
print('Number of rows in postDB : ', len(postDB.index))


# In[5]:


# create the Data Frame
df = pd.DataFrame(data=comDB)
df_post = pd.DataFrame(data=postDB)

df

# add a new colum with sequence numbers
df['Count']=1
df_post['Count']=1

# print all the DF
pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', 5)

df
#df_post


# # Those 2 graphs are examples of explorative analysis you can run
# - It's important to notice the Pandas code (df_post.loc[df_post['Site'] == 'FB']) used to extract a subset of the whole data frame. We will need to do this procedure many times, try to think about other possible subsets.
# - The "campaign type" variable used in this graph is an example of this database's manually coded variables. This variable required 10 persons for 1 week to be appropriately coded (each content - 10k post/tweet - has been coded twice).
# 

# In[6]:


# take the right part of the df
# this create 2 variables (y and z) that we will compare in the graph

z = df_post.loc[df_post['Site'] == 'FB']
z = z.groupby(['p_campagna']).count()
z = z.Count.transform(lambda x: x/x.sum()*100).round(1)  # make the percentage

y = df_post.loc[df_post['Site'] == 'Twitter']
y = y.groupby(['p_campagna']).count()
y = y.Count.transform(lambda x: x/x.sum()*100).round(1)  # make the percentage



# collect the labels and place them under the two variables
labels = z.index   # the text of the lables
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

# graph creation and axis creation  
fig, ax = plt.subplots(figsize=(8,5), dpi=100)

rects1 = ax.bar(x - width/2, z, width, label='Facebook', color='#3b5998', error_kw=dict(elinewidth=6, ecolor='yellow'))
rects2 = ax.bar(x + width/2, y, width, label='Twitter', color='#00aced', error_kw=dict(elinewidth=6, ecolor='yellow'))

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percentage of political campaing \n (% of total post for each social media)')
ax.set_title('Twitter and Facebook: the different usage of political campaign')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# bar labels function
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
        
autolabel(rects1)
autolabel(rects2)

# plot the graph
fig.tight_layout()
plt.savefig('Campaign_per_social_media.png', dpi=300)
plt.show()

# short explanation of the graph
print('This graph represents the different use of the 4 campaign types (comparative, negative, neutral and positive).\nWe can see that politicians use more comparative and positive campaigns on Facebook \n and more negative campaign on Twitter. \nIt probably depends on the smaller amount of words you can post on Twitter.')


# # Some additional reflections
# - This is one of my master thesis's preliminary results: the hate speech comments are significantly more when answering negative and comparative political communication posts/tweets. 
# - Because of the temporal line (before the politician makes the post, after the citizen answer to it), we can hypothesize causality between the political communication and the hate comments.
# - Be aware that positive posts are much more than comparative and negative. That's mean the effect is more significant than what it seems from this graph; you can try to plot the absolute numbers of each type of political campaign to get an idea.

# In[11]:


# Take the right subset, in this case the hate speech comments 
# in relation the type of campaign they answer to
y = comDB.loc[comDB['c_rating'] == 'hate']
y = y.groupby(['p_campagna']).count()
y = y.Count.transform(lambda x: x/x.sum()*100).round(1)


# create the lables and set the graph
labels = y.index
plt.rcParams['font.size'] = 14 
sizes = y
colors = ['orange', 'red', 'lightgreen', 'green']
explode = (0.0, 0.1, 0.0, 0)  # explode 1st slice


# Plot the graph
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)


# plot some titles
plt.axis('equal')
plt.title('Tot hate speech contents for type of political campaign', 
          fontsize='20', 
          loc='center',
          #backgroundcolor='red', 
          color='red',
          y=1.05)


#save the result
plt.savefig('hate_speech_per_campaign.png', dpi=950)

plt.show()

