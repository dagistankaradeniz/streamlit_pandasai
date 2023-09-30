import pandas as pd
from pandasai import SmartDatalake

# Sample DataFrames
df1 = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia",
                "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504,
            1490967855104, 4380756541440, 14631844184064],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})
df2 = "https://raw.githubusercontent.com/nmeraihi/data/master/Loan%20payments%20data.csv"

dl = SmartDatalake([df1, df2])

dl.chat('Which are the 5 happiest countries?')
