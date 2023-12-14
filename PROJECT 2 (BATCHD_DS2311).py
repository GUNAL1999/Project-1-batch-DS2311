#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT

# In[1]:


import pandas as pd


# In[2]:


import re


# In[3]:


import regex as re


# In[4]:


#print(help(re))


# In[5]:


for i in dir(re):
    print(i,end=",")


# In[6]:


print(len(dir(re)))


# QUESTION 1

# In[8]:


string1='Python Exercises,PHP:exercise'
x=re.sub("[ ,.]",":",string1)
print(x)


# QUESTION 2

# In[9]:


data={'SUMMARY':['hello,world!','XXXXXtest','123four,five:;six...']}
df=pd.DataFrame(data)
df['SUMMARY']=df['SUMMARY'].apply(lambda x:re.sub(r'[^\w\s]','',x))
print(df)


# QUESTION 3

# In[21]:


import re


# In[26]:


def find_long_words(string):
    pattern=re.compile(r'\b\w{4,}\b')
    long_words=pattern.findall(string)
    return long_words
string="india is one of the developing country in the world"
result=find_long_words(string) 
print(result)                   


# In[ ]:





# QUESTION 4

# In[28]:


def find_long_words(string):
    pattern=re.compile(r'|b\w{3,5}\b')
    matches=pattern.findall(string)
    return matches
string="india is one of the developing country in the world"
result=find_long_words(string)
print(result)


# QUESTION 5

# In[40]:


import re


# In[43]:


def remove_parantheses(strings):
    pattern=re.compile(r'\([^)*\)')
    return[pattern.sub('',s)for s in strings]
sample_text["example(.com)","hr@fliprobo (.com)","Hello(Data Science World)","Data (Scientists)"]
result=remove_parantheses(sample_text)
print(result)


# QUESTION 7

# In[46]:


sample_text="ImportanceOfRegularExpressionsInPython"
result=re.findall('[A-Z][^A-Z]*',sample_text)
print(result)


# QUESTION 8

# In[50]:


sample_text="RegularExpression1IsAn2ImportantTopic2InPython"
pattern=r'(\d+)([A-Za-z]+)'
result=re.sub(pattern,r'\1\2',sample_text )
print(result)              


# QUESTION 9

# In[2]:


import re


# In[11]:


sample_text="RegularExpressions1IsAn2ImportantTopic3InPython"
pattern=r'([A-Z][a-z0-9]+||d+)'
result=re.sub(pattern,r'\1',sample_text)
result=result.strip()
print(result)


# QUESTION 11

# In[12]:


def match_string(string):
    pattern=r'^[a-za-z0-9_]+$'
    if re.match(pattern,string):
        return True
    else:
        return False


# In[14]:


string1=("Data sciemce deals with AI and Mchine learnig")
#output:string1 matches the pattern


# QUESTION 12

# In[15]:


def starts_with_number(string,number):
    if string.startswith(str(number)):
        return True
    else:
        return False
    


# QUESTION 13

# In[16]:


ip="485.09.0369.150"
string=re.sub('\.[0]*','.',ip)
print(string)


# QUESTION 14 

# In[25]:


sample_text="On August 15th 1947 that India was declared independent from British colonialism and the reins of control were handed over to the leaders of the country"
pattern=r"\b([A-Z][a-z]+)\d{1,2}(?:st|nd|rd|th)?s+\d{4}\b"
matches=re.findall(pattern,sample_text)
print(matches)


# QUESTION 15

# In[3]:


def search_literals(text,searched_words):
    found_words=[word for word in searched_words if word in text]
    return found_words

sample_text='The quick brown fox jumps over the lazy dog'
searched_words=['fox','dog','horse']
result=search_literals(sample_text,searched_words)
print("Found Words:",result)


# QUESTION 16

# In[5]:


import re


# In[6]:


pattern='fox'
text='The quick brown fox jumps over the lazy dog'
match=re.search(pattern,text)
s=match.start()
e=match.end()
print('Found "%s" in %s" from %d to %d' % (match.re.pattern,match.string,s,e))


# QUESTION 17

# In[8]:


sample_text='Python exercises,PHP exercises,C# exercises'
pattern='exercises'
for match in re.findall(pattern,sample_text):
    print('Found "%s"' %match)


# QUESTION 18

# In[13]:


sample_text='Python exercises,PHP exercises,C# exercise'
pattern='exercises'
for match in re.finditer(pattern,sample_text):
    s=match.start()
    e=match.end()
    print('Found "%s" at %d:%d' % (sample_text[s:e],s,e))


# QUESTION 20

# In[15]:


import re


# In[18]:


def find_decimal_numbers(string):
    pattern=re.compile(r'\d+\.\d{1,2}')
decimal_numbers=re.findall(pattern,string)
return decimal_numbers
sample_text="001.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
output=find_decimal_numbers(sample_text)
print(output)                       
                                               
                       


# QUESTION 21

# In[20]:


text="Hundred 100, Two Hundred 200, Three Hundred 300"
result=re.split("\D+",text)
print(result)


# QUESTION 22

# In[22]:


sample_text='My marks in each semester are:947,896,926,524,734,950,642'
number=re.findall('\d+',sample_text)
number=map(int,number)
print("Max_value",max(number))


# QUESTION 23

# In[30]:


sample_text="RegularExpressionIsAnImportantTopicInPython"
x=re.split("\s",sample_text)
print(x)


# QUESTION 24

# In[31]:


text="AbCdEFgHi"
pattern=re.compile(r'([A-Z][a-z]+)')
matches=re.findall(pattern,text)
print(matches)


# QUESTION 25

# In[33]:


sample_text="Hello hello world world"
x=re.sub(r'(\w+)\1',r'1',sample_text)
print(x)


# QUESTION 26

# In[34]:


def check_string(string):
    pattern=r"\w$"
    match=re.search(pattern,string)
    if match:
        return True
    else:
        return False


# QUESTION 27

# In[40]:


def extract_hashtags(text):
    hashtags=re.findall(r'#\w+',text)
    return hashtags
sample_text='RT @kapil_kaushik:#Doltwal I mean #xyzabc is "hurt"by #Demonitaization as the same has rendered'
hashtags=extract_hashtags(sample_text)
print(hashtags)


# QUESTION 28

# In[42]:


sample_text="@Jags123456Bharat band on 28??<ed><U+00A0><U+00B8><ed><U+00b8><U+0082>Those who are protesting#demonetization are all difgferent party leaders"
pattern=r"<U\=\w{4}>"
output_text=re.sub(pattern,"",sample_text)
print(output_text)


# QUESTION 29

# In[47]:


open('filename.txt','r') as
file:
    text=file.read
text=Ron was born on 12-9-1992 and he was admitted to school 15-12-1999
pattern=r'\d{2}\-d{2}-\d{4}'
dates=re.findall(pattern,sample_text)
print(date)


# QUESTION 30

# In[49]:


def remove_words(string):
    pattern=re.compile(r'\b\w{2,4}\b')
    modified_string=re.sub(pattern,'',string)
    return modified_string


# In[52]:


sample_text="The following example creates an ArrayList with a caopacity of 50 elements.4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly"
result=remove_words(sample_text)
print(reuslt==expected_output)
#true


# In[ ]:




