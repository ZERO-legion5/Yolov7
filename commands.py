import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

def show_chart(data,title):

    sns.histplot(data, kde=True)
    plt.xlabel('People Count')
    plt.ylabel("Frequency")
    plt.title("Histogram of Data")
    plt.savefig(f"{title}.png")

def save_to_json(k,title):

    with open('data.json','r') as f:

        m = json.load(f)

    with open('data.json','w') as f:

        m[title] = k['person']
        m[title+'violence'] = k['violence']
        m[title+'weapons'] = k['weapons']
        m[title+'work'] = k['work']
        json.dump(m,f)