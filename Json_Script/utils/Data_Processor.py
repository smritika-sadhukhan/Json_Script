import json
import numpy as np
import pandas as pd
def data_Processer(data): 
 list3=[]
 list11=[]
 list22=[]
 list33=[]
 for p in range(0,len(data['Hotel_Dataset'])):
  
   list1=[]
   list2=[]
   if len(data['Hotel_Dataset'][p]['entity'])!=0:
    for i in data['Hotel_Dataset'][p]['entity']:
    
      a=i['Start_Token']-1
      b=i['End_Token']
      if a>0:
       for k in range(len(list1),a):
     
      
        list1.append((data['Hotel_Dataset'][p]['text'].split()[k],'O'))
      
        list33.append(p)
       
        list11.append(data['Hotel_Dataset'][p]['text'].split()[k])
       
        list22.append('O')
     
      c=0
      for m in i['Value'].split():
        c=c+1
        if c>1:
          A=('I-'+i['Entity'])
        else:
          A=('B-'+i['Entity'])

        list1.append((m,A))
     
        list11.append(m)
        list33.append(p)
        list22.append(A)
        
    if len(list1)<len(data['Hotel_Dataset'][p]['text'].split()):
          for kk in range(len(list1),len(data['Hotel_Dataset'][p]['text'].split())):
           
          
            list1.append((data['Hotel_Dataset'][p]['text'].split(' ')[kk],'O'))
            
    else:
        for kk in range(0,len(data['Hotel_Dataset'][p]['text'].split())):
            list1.append((data['Hotel_Dataset'][p]['text'].split(' ')[kk],'O'))
    list3.append(list1)
  
 df=pd.DataFrame()
 df['sentences']=list33
 df['words']=list11
 df['tags']=list22
 list111=[]
 list222=[]

 for ii in list3:
   list_1=[]
   list_2=[]

   for jj in ii:
     list_1.append(jj[0])
     list_2.append(jj[1])
   list111.append(' '.join(list_1))
   list222.append(' '.join(list_2))
 df1=pd.DataFrame()
 df1['query']=list111
 df1['label']=list222
 return(df,df1,list3)

def NLU_creator(data,action=1,previous_intent=1):
  intent=[]
  text=[]
  for i in data['Hotel_Dataset']:
    intent.append('+'.join(i['intent']))
    text.append(i['text'])
  NLU=pd.DataFrame()
  NLU['text']=text
  NLU['intent']=intent
  fff=[]
  for i in data['Hotel_Dataset']:
    dict12={}
    for j in i:
      if j=='text':
          
          if  previous_intent==1 and action==1:
              dict12['previous_intent']=i[j].split()[0][:-1]
              dict12['action']=i[j].split()[1][:-1]
              dict12[j]=' '.join(i[j].split()[2:])
          elif  previous_intent==1 and action==0:
              dict12['previous_intent']=i[j].split()[0][:-1]
              dict12[j]=' '.join(i[j].split()[1:])
          elif  previous_intent==0 and action==1:
              dict12['action']=i[j].split()[0][:-1]
              dict12[j]=' '.join(i[j].split()[1:])
      else:
          dict12[j]=i[j]
    fff.append(dict12)
  return fff,NLU
