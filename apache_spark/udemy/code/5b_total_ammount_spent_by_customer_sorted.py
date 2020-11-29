'''
author: faraz mazhar
descri: Solution of the first assginment but output is sorted by amount spent.
'''

from pyspark import SparkConf, SparkContext

def parse_line(line):
    '''
    This function takes an argument, splits it by comma, and returns `customer_id` and `price`.
    '''
    customer_id, _, price = line.split(',')
    return (int(customer_id), float(price))

conf = SparkConf().setMaster('local').setAppName('totalAmmountSpentByCustomers')
sc = SparkContext(conf=conf)

orders_rdd = sc.textFile('customer-orders.csv')

results = orders_rdd.map(parse_line) \
    .reduceByKey(lambda x, y: x + y) \
    .map(lambda x: (x[1], x[0])) \
    .sortByKey() \
    .collect()

for result in results:
    print(result)

'''
SORT BY KEY
(3309.38, 45)
(3790.570000000001, 79)
(3924.230000000001, 96)
(4042.6499999999987, 23)
(4172.289999999998, 99)
(4178.500000000001, 75)
(4278.049999999997, 36)
(4297.260000000001, 98)
(4316.299999999999, 47)
(4327.729999999999, 77)
(4367.62, 13)
(4384.33, 48)
(4394.599999999999, 49)
(4475.569999999999, 94)
(4505.79, 67)
(4517.27, 50)
(4524.509999999999, 78)
(4561.069999999999, 5)
(4628.4, 57)...
'''
