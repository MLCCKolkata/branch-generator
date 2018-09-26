'''
Author: Adrish Dey
Website: https://member.acm.org/~adrishd
Date: 26th September, 2018

'''
import pandas as pd
import shutil
import numpy as np
import os
import subprocess,shlex
import time
df=pd.read_csv("MLCC Assignments.csv")
df.rename(columns={"Github ID":"github"},inplace=True)
df["github"]=df["github"].apply(lambda x:str(x).split(".com/")[-1].split('/')[0])
# For this slot of first 86 people
#df2=pd.DataFrame(columns=df.columns)
#errors=[6,74]
#for i in errors:
#    df2=df2.append(df.iloc[i])
#df.drop(errors,inplace=True)
#df.to_csv("eligible.csv")
#df2.to_csv("not-eligible.csv")
os.chdir("Assignment-3")
#generic branching code
for account in df["github"]:
    l=[0 for _ in range(6)]
    l[0]=subprocess.Popen(shlex.split("git checkout master")).wait()
    l[1]=subprocess.Popen(shlex.split("git branch {}".format(account))).wait()
    if l[1]:
        continue
    l[2]=subprocess.Popen(shlex.split("git checkout {}".format(account))).wait()
    shutil.copy("../base.ipynb","{}.ipynb".format(account))
    l[3]=subprocess.Popen(shlex.split("git add -A")).wait()
    l[4]=subprocess.Popen(shlex.split("git commit -a -m 'Code Committed for {}'".format(account))).wait()
    l[5]=subprocess.Popen(shlex.split("git push origin {}".format(account))).wait()
    print(account,"->","success" if sum(l)==0 else "Failed! in step",np.argmax(abs(np.array(l)))+1)
    print("\n\n\n\n\n")
