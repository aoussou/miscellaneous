#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:23:29 2017

@author: JohnJohn
"""

'''
This code can be useful to memorize long texts, such as scriptures. 
A tool called imemorize (check http://www.imemorize2.org/) exists that is much 
more sophisticated, however I found that:

- it is efficient enough to hide every other word. You can get two 
complementary versions, e.g.: if you're text is "a b a b a b", version 1 is 
"a _ a _ a _" and version 2 is the complement "_ b _ b _ b".

- it is not productive to hide common words such as "is", "the", "a"... The 
most important is to hide nouns, verbs and adjectives.

EXAMPLE:
    
You want to memorize the following passage:
    
"It is not for him to pride himself who loveth his own country, but
rather for him who loveth the whole world. The earth is but one country, and 
mankind its citizens."

The code will output:

==============
VERSION 1 

It is not for him to _ _ _ _ _  himself who _ _ _ _ _ _  his own
 _ _ _ _ _ _ _ , but rather for him who _ _ _ _ _ _  the whole _ _ _ _ _ . 
The earth is but _ _ _  country, and _ _ _ _ _ _ _  its citizens.

==============
VERSION 2 

It is not for him to pride _ _ _ _ _ _ _  who loveth his _ _ _  country, 
but _ _ _ _ _ _  for him who loveth the _ _ _ _ _  world. The _ _ _ _ _  is but
 one _ _ _ _ _ _ _ , and mankind its _ _ _ _ _ _ _ _ .

'''

text = input('''Input your text here. If you want to use the above example
just press ENTER: ''') 

if text == '':

   text = """It is not for him to pride himself who loveth his own country, 
    but rather for him who loveth the whole world. The earth is but one 
    country, and mankind its citizens."""

# Choose what words don't need to be hidden
connectors = {
        "he","him","his","He","Him","His"
        "It","is","it","the","a","that","in","to","of","this","and","which",
        "or","A","The","as","into","It","its","not","who","for","but","he"} 

# Don't hide punction
punctuation = {".",",",":","!","?"}

def make_blank(text,connectors,punctuation,skip_int):
    
    s = text.split() 
    k = 0
    k_last_del = skip_int;
    
    for i in range(0,len(s)):
             
        if (k%2) == skip_int:
    
            if s[i] not in connectors :
            
                k_last_del = k;
                
                if s[i][-1] not in punctuation :
                    s[i] = "_ "*len(s[i])
                    
                else:
                    ls = list(s[i])
                    ls[0:len(s[i])-1] = "_ "*(len(s[i])-1)
                    s[i] = str("".join(ls))                
            else:
                k = k+1
                
        elif s[i] in connectors and (k_last_del%2) == skip_int:
                        k = k+1
                    
        k = k+1
        
    return " ".join(s)

print('\n==============')
print('VERSION 1 \n')

print(make_blank(text,connectors,punctuation,0))

print('\n==============')
print('VERSION 2 \n')

print(make_blank(text,connectors,punctuation,1))
