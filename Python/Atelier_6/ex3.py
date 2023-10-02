from datetime import datetime

# datetime_str = '09/19/22 13:55:26'

# datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

# print(type(datetime_object))
# print(datetime_object)  # printed in default format



def filtrer_par_date(transactions, date_debut, date_fin):
    transactions_filtrees = []
    for transaction in transactions:
        if transaction[date]>= date_debut and transaction[date] <= date_fin:
            transactions_filtrees.append(transaction)
    return transactions_filtrees
