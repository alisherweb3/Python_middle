import pandas as pd
df = pd.read_csv('prices.txt', sep='\t', header = None)
df.columns = ['Товар', 'Количество', 'Цена']
df['Итого'] = df['Количество'] * df['Цена']
summa_zakaza = sum(df['Итого'])
print(summa_zakaza)
