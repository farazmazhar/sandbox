'''
This is a solution of the first assginment of Udemy PySpark course by Frank Kane.
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
    .collect()

for result in results:
    print(result)
    