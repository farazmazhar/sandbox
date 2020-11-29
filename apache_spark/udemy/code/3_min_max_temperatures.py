'''
Minimum temperature by location.
'''

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf=conf)

def parseLine(line):
    '''
    Parses CSV formatted line.
    '''
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0 # F
    return (stationID, entryType, temperature)

lines = sc.textFile("1800.csv")
parsedLines = lines.map(parseLine)
minTemps = parsedLines.filter(lambda x: "TMIN" in x[1])
stationTemps = minTemps.map(lambda x: (x[0], x[2]))
minTemps = stationTemps.reduceByKey(min)
tmin = minTemps.collect()

# Modifications made to get max temperature.
tmax = lines \
    .map(parseLine) \
    .filter(lambda x: "TMAX" in x[1]) \
    .map(lambda x: (x[0], x[2])) \
    .reduceByKey(max) \
    .collect()

print('Minimum temperature...')
for result in tmin:
    print(result[0] + "\t{:.2f}F".format(result[1]))

print('Maximum temperature...')
for result in tmax:
    print(result[0] + "\t{:.2f}F".format(result[1]))
