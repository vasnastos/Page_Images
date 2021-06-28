# Data for all the carter Dataset Files
from importlib import resources as pck_res 
from tabulate import tabulate
from pickle import load
import os

class CarterDataSet:
    def __init__(self,fn,students,periods,exams,enrolls,cost):
        self.filename=fn
        self.students=students
        self.periods=periods
        self.exams=exams
        self.enrollments=enrolls
        self.cost=cost

    def __str__(self):
        return self.filename+','+str(self.students)+','+str(self.periods)+','+str(self.exams)+','+str(self.enrollments)


datasets=dict()
datasets['car-f-92']=CarterDataSet('car-f-92.stu',18419,32,543,55522,3.71)
datasets['car-s-91']=CarterDataSet('car-s-91.stu',16925,35,682,56877,4.39)
datasets['ear-f-83']=CarterDataSet('ear-f-83.stu',1125,24,190,8109,32.63)
datasets['hec-s-92']=CarterDataSet('hec-s-92.stu',2823,18,81,10632,10.04)
datasets['kfu-s-93']=CarterDataSet('kfu-s-93.stu',5349,20,461,25113,12.90)
datasets['lse-f-91']=CarterDataSet('lse-f-91.stu',2726,18,381,10918,9.82)
datasets['pur-s-93']=CarterDataSet('pur-s-93.stu',30029,42,2419,120681,4.49)
datasets['rye-s-93']=CarterDataSet('rye-s-92.stu',11482,23,486,45051,7.93)
datasets['sta-f-83']=CarterDataSet('sta-f-83.stu',611,13,139,5751,157.03)
datasets['tre-s-92']=CarterDataSet('tre-s-92.stu',4360,23,261,14901,7.72)
datasets['uta-s-92']=CarterDataSet('uta-s-92.stu',21266,35,622,58979,3.04)
datasets['ute-s-92']=CarterDataSet('ute-s-92.stu',2749,10,184,11793,24.77)
datasets['yor-f-83']=CarterDataSet('yor-f-83.stu',941,21,181,6034,34.71)


def statistics():
    pathfile=os.path.join('','Stats')
    files=os.listdir(pathfile)
    counter=1
    for file in files:
        print(f'{counter}.{file}')
        counter+=1
    choice=int(input('Select a file:'))
    print('\n\n')
    data=list()
    headers=list()
    with open(os.path.join(pathfile,files[choice-1]),'r') as F:
        start=True
        for line in F:
            if len(line.strip())==0:
                continue
            if start:
                start=False
                headers=line.strip().split(',')
                continue

            data.append(line.strip().split(','))
    
    print(tabulate(data,headers=headers,tablefmt='fancy_grid'))

def get_best_cost():
    return {dataset:datasets[dataset].cost for dataset in datasets}


