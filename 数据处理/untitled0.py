# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:52:51 2019

@author: Administrator
"""

import pandas as pd
import numpy as np
a=pd.DataFrame(np.ones([3,3]))
a.iloc[2,1] = np.NaN
a.iloc[:,0] = [5,6,7]
a.iloc[:,2] = [12412412412,67832452354,56234234236]
a.fillna({'b':5})
a.columns=['a','b','c']
a['b'].str.strip()
a['c']=a['c'].astype(str)
a
a['c'].str.slice(1,3)
a=a.set_index('a')
a.reset_index(drop=True)

