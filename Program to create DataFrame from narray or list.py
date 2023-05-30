#Program to create DataFrame from narray/list
 
import pandas as pd
 
data = {'Name':['Akshat', 'Ansh', 'Shrey', 'Saurabh', 'Vinay'],
        'Age':[21, 21, 19, 19,20]}
df = pd.DataFrame(data)

print(df)
