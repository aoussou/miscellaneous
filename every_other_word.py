'''

This code can be useful to memorize long texts, such as scriptures. 
A tool called imemorize (check http://www.imemorize2.org/) exists that is much 
more sophisticated, however I found that:

- It is enough to hide every other word. You can get two complementary 
versions, e.g.: if you're text is "a b a b a b", version 1 is "a _ a _ a _" and
version 2 is the complement "_ b _ b _ b"

- It is not productive to hide common words such as "is", "the", "a"... The 
most important is to hide nouns, verbs and adjectives

'''

text = ''''It is not for him to pride himself who loveth his own country, but
rather for him who loveth the whole world. The earth is but one country, and 
mankind its citizens.'''

# Uncomment the line below to input your text in the console. 
# DO NOT forget to delete the other text'''
#text = input('Input your text here: ') 


# Choose what words don't need to be hidden
connectors = {"is","it","the","a","that","in","to","of","this",
            "and","which","or","A","The","as","into"} 

# Don't hide punction
punctuation = {".",",",":","!","?"}

s = text.split() 
k_last_del = 0;
skip_int = 0
k = skip_int

for i in range(0,len(s)):
         
    if (k%2) != skip_int:

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
            
    elif s[i] in connectors and (k_last_del%2) != skip_int:
                    k = k+1
                
    k = k +1
           
sj = " ".join(s)

print(sj)