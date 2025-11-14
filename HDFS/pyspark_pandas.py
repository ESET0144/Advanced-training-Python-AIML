import pandas as pd

data = {"a": [1, 2, 3], "b":["uday", "raj", "ravi"], "c": ["p", "q", "r"]}

df = pd.DataFrame(data)
print(df)


import pyspark.pandas as ps

df2 = ps.DataFrame(data)
print(df2)


