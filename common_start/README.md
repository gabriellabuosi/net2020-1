# First week - common start - play with data
### This is the folder with the data and scripts for the first week of the group project.

The idea of this first week is to take confidence with the data.
You can try to import the .csv file and make some general graphs to be sure you understood as much as possible the main variables involved.
You can use our telegram chat as a forum to report issues about the DB.

```common_start.py``` is the same script as ```common_start.ipynb```, the second one is in Jupiter Notebook format.

The file contains some information about the database.
I also made two general graphs that will show you two main results of my master thesis. 
Take them as examples of what you could do for a generical description of the DB.

### You can try the script
To use the script you should:
- clone the directory ```git clone git@github.com:SalvatoreRomano1/net2020.git```
- download the ["databese" folder](https://drive.google.com/drive/folders/1q6U4JlQadPKRWbAAeXQsRTcVX4PSlG0b?usp=sharing) from the shared G.drive 
- copy it to net2020/common_start/
- change the path of the DB in the script line 20 and 23
- run the script


### Some idea for introductive analysis
Once you run the code, you can add some initial analysis to understand this database's potential better.
Some examples could be:

For semantic network group
- try to generate some [WordCloud](https://amueller.github.io/word_cloud/auto_examples/index.html#example-gallery). You can also create some [fency ones](https://github.com/amueller/word_cloud). This will allow you to start creating some subsets of the data frame and get an idea of the words we will be working with. This is just a way to get the first idea; the text cleaning procedure (stopwords removal, lemmatization...) is unnecessary. We will do it in the next weeks.
- you could plot the WordCloud of the subset of the hate speech comments (``` comDB.loc[comDB['c_rating'] == 'hate']```)
- you could plot general WordCloud of all the comments and compare it with the WordCloud of all the politicians' posts/tweets

For post network group
- try to understand how much content we have for the most relevant subsets. How many hate speech comments (``` comDB.loc[comDB['c_rating'] == 'hate']```) do we have? How many politicians do we have? How many comments for each political party has been collected? 
- you could try to use the information in the columns with the sentiment analysis values (they are at the end of the df, from ```c_WC``` till the end). Each comment has a value from 0 to 100, representing a specif sentiment. For example, the variable ```c_Emo_Neg```tells us the level of negative emotions detected in the comment, ```p_Emo_Neg``` tell us the same thing for the posts. What is the average sentiment of the negative emotions in the politicians' posts? And which one is the average of negative emotions along with all the comments? 

Have fun!
