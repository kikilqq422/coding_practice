import pandas as pd
import numpy as np
def adder(x1,x2):
    return x1+x2
df = pd.DataFrame(np.random.randn(4,3,columns=['c1','c2','c3']))
#传入自定义函数以及要相加的数值3
df.pipe(adder,3)