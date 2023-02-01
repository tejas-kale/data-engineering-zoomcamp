import numpy as np
import pandas as pd
import sys
from tabulate import tabulate

mu: float = float(sys.argv[1])
sigma: float = float(sys.argv[2])

np.random.seed(42)
df = pd.DataFrame({
    'date': pd.date_range('2022-01-01', periods=10, freq='1D'),
    'value': mu + sigma * np.random.randn(10)
})

print(tabulate(df, headers='keys', tablefmt='psql'))