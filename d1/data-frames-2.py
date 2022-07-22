import pdb


'''
Signup Rate, Cancel_rate, Subscription Rate

https://www.kaggle.com/code/candycrash/customer-subscription-eda-and-prediction


cust_prod = pd.read_csv('data/dspp1/customer_product.csv')
cust_case = pd.read_csv('data/dspp1/customer_cases.csv')
cust_info = pd.read_csv('data/dspp1/customer_info.csv')
prod_info = pd.read_csv('data/dspp1/product_info.csv')


We have a dataset which has product sign-ups and cancellations by customers.
    Unnamed: 0 customer_id product     signup_date_time     cancel_date_time
0   1       C2448   prd_1  2017-01-01 10:35:09                  NaN
1   2       C2449   prd_1  2017-01-01 11:39:29  2021-09-05 10:00:02
2   3       C2450   prd_1  2017-01-01 11:42:00  2019-01-13 16:24:55
3   4       C2451   prd_2  2017-01-01 13:32:08                  NaN
4   5       C2452   prd_1  2017-01-01 13:57:30  2021-06-28 18:06:01

Task 1: 
Please calculate the duration in number of days how long customer used the product. 
if any customer doesn't have cancel_date_time, duration must be calculated up-to till date.

Task 2:
In this dataset, we have two products. 
prd_1 is for annual_subscription and has one year billing cycle.
prd_2 is for monthly_subscription and has one month billing cycle.

Please find out, how many billing cycles have been paid by each customers

Task 3:
In this dataset, we have two products. 
prd_1 is for annual_subscription and has one year billing cycle.
prd_2 is for monthly_subscription and has one month billing cycle.

We calculate the amount how much each customer has paid till now.
Price is 12$ per month and customer will get 10% discount on annual subscription.

Now please modify the code to find out top 10 highly paid active customers.

'''
# import pdb
# import numpy as np
# import pandas as pd
# from datetime import datetime as dt

# cust_prod = pd.read_csv('data/dspp1/customer_product.csv')
# cust_prod = cust_prod.drop(columns='Unnamed: 0')
# cust_prod = cust_prod.drop_duplicates(subset=['customer_id', 'product', 'signup_date_time'], keep='first')
# cust_prod['cancel_date'].fillna(dt.today(), inplace=True)

# cust_prod['signup_date'] = cust_prod['signup_date_time'].astype('datetime64').dt.date.astype('datetime64')
# cust_prod['cancel_date'] = cust_prod['cancel_date_time'].astype('datetime64').dt.date.astype('datetime64')
# cust_prod.drop(columns=['signup_date_time', 'cancel_date_time'], inplace=True)

# cust_prod['duration'] = (cust_prod['cancel_date'] - cust_prod['signup_date']).dt.days.astype('int64')
# print(cust_prod)
# exit()



import pdb
import numpy as np
import pandas as pd
from datetime import datetime as dt

cust_prod = pd.read_csv('data/dspp1/customer_product.csv')
cust_prod = cust_prod.drop(columns='Unnamed: 0')
cust_prod = cust_prod.drop_duplicates(subset=['customer_id', 'product', 'signup_date_time'], keep='first')

cust_prod['signup_date'] = cust_prod['signup_date_time'].astype('datetime64')
cust_prod['cancel_date'] = cust_prod['cancel_date_time'].astype('datetime64')
cust_prod['cancel_date'].fillna(dt.today(), inplace=True)
cust_prod.drop(columns=['signup_date_time', 'cancel_date_time'], inplace=True)

cust_prod['signup_year'] = cust_prod['signup_date'].dt.year.astype('int64')
cust_prod['signup_month'] = cust_prod['signup_date'].dt.month.astype('int64')
cust_prod['cancel_year'] = cust_prod['cancel_date'].dt.year.astype('int64')
cust_prod['cancel_month'] = cust_prod['cancel_date'].dt.month.astype('int64')

cust_prod["total_months"] = (cust_prod['cancel_year'] - cust_prod['signup_year']) * 12
cust_prod["total_months"] += (cust_prod['cancel_month'] - cust_prod['signup_month'])

cust_prod.loc[cust_prod["product"] == "prd_1", "cycles"] = 12
cust_prod.loc[cust_prod["product"] == "prd_2", "cycles"] = 1
cust_prod["cycles"] = (cust_prod["total_months"] / cust_prod["cycles"]).astype(int)

price = 12
cust_prod.loc[cust_prod["product"] == "prd_1", "amount"] = cust_prod["cycles"] * price * 12
cust_prod.loc[cust_prod["product"] == "prd_1", "amount"] = cust_prod["amount"] - cust_prod["amount"] * .1
cust_prod.loc[cust_prod["product"] == "prd_2", "amount"] = cust_prod["cycles"] * price

amounts_paid = cust_prod.sort_values("amount", ascending=False).head(10)
print(amounts_paid)

