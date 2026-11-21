import numpy as np
import pandas as pd

def loaded_Data():
    raw_data = {
        "Product" : ["Laptop","Keyboard","Mouse","Monitor","Laptop","Mouse",None],
        "Catetory" : ["Electornics","Accessories","Electornics","Electornics","Accessories","Accessories","Accessories"],
        "Quantity" : [2,4,10,5,8,np.nan,20],
        "Price" : [100,300,800,200,101,550,600]
    }

    return pd.DataFrame(raw_data)