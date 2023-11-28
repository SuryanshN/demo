# q1 write a prior algorithm with python code

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import pandas as pd
# Define a list of transactions
transactions = [['apple', 'banana', 'cherry'],
                ['apple', 'banana'],
                ['banana', 'cherry'],
                ['apple', 'banana', 'cherry', 'orange'],
                ['cherry', 'orange']]

# Initialize a transaction encoder
te = TransactionEncoder()

# Transform the list of transactions into a one-hot encoded boolean array
te_ary = te.fit(transactions).transform(transactions)

# Convert the boolean array into a pandas DataFrame
df = pd.DataFrame(te_ary, columns=te.columns_)

# Find frequent itemsets using the Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)

# Print the frequent itemsets
print(frequent_itemsets)
