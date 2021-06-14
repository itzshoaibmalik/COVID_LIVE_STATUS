# Made by Shoaib MAlik
# Designed on OS

'''
COVID LIVE TRACKER BY SHOAIB MALIK
'''

import subprocess,sys
def install(package):
    subprocess.call([sys.executable, "-m","pip","--disable-pip-version-chec","-q", "install", package])

install("requests")
install("matplotlib")
import requests, json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

frame1 = plt.gca()

data = requests.get('https://www.trackcorona.live/api/countries')
json = data.json()
def num(x):
    if x >= 1000 and x < 999999:
        return str((x//100)/10)+'K'
    elif x >= 1000000:
        return str((x//100000)/10)+'M'
    else:
        return x

ls_co = {}
ls_re = {}
ls_de = {}
total_confirm = 0
total_recover = 0
total_death = 0
for i in json['data']:
    loc = i['location']
    if len(i['location']) > 20:
        loc = i['location'][0:18]+'...'
    ls_co[loc] = num(i['confirmed'])
    ls_re[loc] = num(i['recovered'])
    ls_de[loc] = num(i['dead'])
    total_confirm += i['confirmed']
    total_recover += i['recovered']
    total_death += i['dead']
    '''print(i['location'], end=' ')
    print(num(i['confirmed']), end=' ')
    print(num(i['recovered']), end=' ')
    print(num(i['dead']))'''
    
df_data = {
    'Confirmed':ls_co,
    ' Recovered':ls_re,
    ' Dead':ls_de
}
df_data_final = pd.DataFrame(df_data)
print(df_data_final.to_string())
total = total_confirm + total_recover + total_death


plt.bar(['Confirmed','Recovered','Total Death'],[total_confirm,total_recover,total_death],color = ['orange','lime','red'])
ls = [total_confirm,total_recover,total_death]
for index, value in enumerate(ls):
    plt.text(index - len(str(value))/45, value+3000000, str(value))
    plt.text(index - len(str(value))/65, value/2, str(
        str(((value*1000/total)//1)/10)+'%'
    ))
font = {'family':'serif','color':'blue','size':15}
plt.title('Graphical Representation', fontdict = font)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
#plt.gca().spines['top'].set_visible(False)
frame1.axes.get_yaxis().set_visible(False)
#plt.show()
plt.savefig("file.png")
