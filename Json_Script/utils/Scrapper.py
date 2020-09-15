# -*- coding: utf-8 -*-
"""Demo.ipynb
 
Automatically generated by Colaboratory.
 
Original file is located at
    https://colab.research.google.com/drive/1cDW5lWg4gQ5W2zqt50CHJok0S9-Lva7g
 
"""
import numpy as np

def  dataframe_to_txt(df,action,previous_intent):
    list5=[]
    for i in df.values:
      if  action==1 and previous_intent==1 :
           if type(i[0])!=float: 
                s='* '+str(i[0])+', '+i[1][:]+','+i[2][1:]
           else:
                s=i[2]
      elif  action==0 and previous_intent==1 :
           if type(i[0])!=float: 
               s='* '+str(i[0])+','+i[1][1:]
      elif  action==1 and previous_intent==0 :
           if type(i[0])!=float: 
               s='* '+str(i[0])+','+i[1][1:]
      elif  type(i[0])!=float and action==0 and previous_intent==0: 
          s=i[0][1:]
      elif type(i[0])==float:
          pass
      
      list5.append(s)
    return(list5)
def markdown_formatter(s):
    list1=[]
    list2=[]
    b=0
    if '['  in s:
      for i in range(0,len(s)):
      
        if s[i]=='[':
            if s[b]==']':
               list1.append(s[b+1:i])
            else:
                list1.append(s[b:i])
            a=i
        elif s[i]==']':
       
            b=i
            list1.append('_'.join(s[a:b+1].split()))
            if '[' not in s[i:]:
               list1.append(s[i+1:])
      list1=''.join(list1)
    else:
      list1=s
  
  
    return(list1)
    
def intent_balancer(f):  
  f=open('/content/Json_Script/Json_Script/Markdown/mark.txt','r')
  list1=[]
  list2=[]
  for i in f:
      list1.append(i)
  list1=' '.join(list1)
  list1=list1.split('\n')
  c=0
  list22=[]
  list33=[]
  list44=[]
  for j in list1:
    if len(j.split())!=0:
      
      if j.split()[0]=='##':
     
        list33.append(list22)
        list22=[]
        list2.append(c)
        list22.append(j)
        list44.append(j)
 
        c=0
      if j.split()[0]=='*':
        j=markdown_formatter(j)
        list22.append(j)
        list44.append(j)
 
        c=c+1
      elif j.split()[0]=='#':
        list2.append(c)
        list33.append(list22)
        break
    else:
      list22.append(' ')
      list44.append(' ')
 
  list_repeat=[]
  for  i in list2[1:]:
    list_repeat.append((int((max(list2)/i)*(max(list2)/i))))
  return(list33[1:],list_repeat,list44)
 
f=open('/content/Json_Script/Json_Script/Markdown/lookups','r') 
 
def entity_fetcher(f):
  list1=[]
  for i in f:
      list1.append(i)
  list1=' '.join(list1)
  list1=list1.split('\n')
  dict2={}
  for s in list1:
    if len(s.split())!=0:
      if (s.split()[0])!='##' and s.split()[0]!='*' :
        c=0
        for i in s:
          if i==' ':
              c=c+1
          else:
              break
        if c==5:
          key=s.split()
          key='_'.join(key)
          values=[]
        elif c==9:
         values.append('_'.join(s.split()))
         dict2[key]=values
  return(dict2)
 
dict3=entity_fetcher(f)
 
def Data_Generate(f,random1,repeat1,verify):
 list33,list_repeat,list44=intent_balancer(f)
 
 import random
 list1=[]
 list2=[]
 list3=[]
 c=0
 for k in range(0,len(list_repeat)):
    repeat=repeat1*list_repeat[k]
    for s in list33[k]:
      if len(s.split())!=0:
        if (s.split()[0])=='##':
          list2.append(s)
        elif s.split()[0]=='*':
          if len(s.split())==1:
            print('Please remove "',s,' " in the below line')
            print('Line --- >',list44.index(s)+1,s)
            break
          else:
           list2.append(s)
           value=[]
           entity=[]
 
           general_entity=[]
           for i in s.split():
              if '[' in i:
                  if len(i.split('[')[0])!=0:
                      print('Please check ***"',i,'"*** in the below line')
                      print('Line --- >',list44.index(s)+1,s)
                      break
              if i[0]=='(':
                  print('Please check ***"',i,'"*** in the below line')
                  print('Line --- >',list44.index(s)+1,s)
                  break
              if i[0]=='[':
                str=i
                i=i[1:].split('](')
                value=i[0]
                if len(i)==1:
                  print('Please check ***"',i,'"*** in the below line')
                  print('Line --->',list44.index(s)+1,s)
                  break
                else:
 
                  j=i[1][:-1].split(')(')
            
                entity=j[0]
                if len(j)==1:
                  general_entity='others'
                else:
                  if len(j[1].split(')'))==2:
                      print("Please check ",str,' in the below line')
                      print('Line',list44.index(s)+1,s)
                      break
                  else:
                      general_entity=j[1]
                # print(value,entity,general_entity)
                if entity in dict3.keys():
                     mini=min(len(dict3[entity]),repeat)
                     for i in range(0,mini):
                        # print(i)
                        before_keyword, keyword, after_keyword = s.partition(value)
                        if random1==1:
                           i=(random.randint(0, len(dict3[entity])-1))
                           m=before_keyword+dict3[entity][i]+after_keyword
                        m=before_keyword+dict3[entity][i]+after_keyword
                        list2.append(m)
                else:
      
                  if verify==1:
                      print("(",entity,") in",s[2:],"at line number ",list1.index(s)+1," is not found ")
                      import sys
                      sys.exit()
                  else:
                       print("(",entity,") in",s[2:],"at line number ",list1.index(s)+1," is not found ")
    c=c+len(list33[k])                 
 return(list2)
 
def entity_extractor(s):
  dict22={}
  dict12={}
  if len(s.split())!=0:
    if s.split()[0]!='##':
  
       #print(s)
       value=[]
       entity=[]
       text=[]
       list_entity=[]
       list22=[]
       text=[]
       c=0
       general_entity=[]
       for i in s.split():
            c=c+1
            dict12={}
            if i[0]=='[':
                i=i[1:].split('](')
                # print('iiiii',i)
                value=i[0]
                value1=value.replace('_',' ')
                j=i[1][:-1].split(')(')
                entity=j[0]
                if len(j)==1:
                  general_entity='others'
                else:
                  general_entity=j[1]
                dict12['General_Entity']=general_entity
                dict12['Start_Char']=s.index(value)-2
                dict12['End_char']=s.index(value)+len(value)-2
                dict12['Start_Token']=c
                dict12['End_Token']=c+len(value1.split())-1
                if entity=='checkinDay':
                    entity='checkin'
                    dict12['Entity']=entity
                elif  entity=='checkoutDay':
                    entity='checkout'
                    dict12['Entity']=entity
 
                else:
                    dict12['Entity']=entity
 
                dict12['Value']=value1
                list22.append(dict12)
                text.append(value1)
                c=c+len(value1.split())-1
                list_entity.append(entity)
            else:
              text.append(i)
     
       return(list22,' '.join(text),list_entity)
 
def final_script(f,random1,repeat,verify): 
 list2=Data_Generate(f,random1,repeat,verify)
 dict_final={}
 list11=[] 
 dict12={}
 list_entity_final=[]
 list_intent_final=[]
 import pandas as pd
 list2=pd.Series(list2).drop_duplicates().tolist()
 for i in list2:
   dict22={}
   if i.split()[0]=='##':
     
      before_keyword, keyword, after_keyword = i.partition('intent:')
      after_keyword1=after_keyword.split('+')
      dict12['intent']=after_keyword1
    
 
   elif  i.split()[0]=='*':
    ent,text,list_entity=entity_extractor(i[2:]) 
    dict12['entity']=ent
    dict12['text']=text
    dict22=dict12.copy()
    list11.append(dict22)
    list_intent_final.append(after_keyword)
    for i in list_entity:
      list_entity_final.append(i)
    dict_final=(list11)
  
 return(dict_final,list_entity_final,list_intent_final)
 

