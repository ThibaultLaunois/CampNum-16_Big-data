from pyspark import SparkContext
from pyspark import read

df = spark.read.csv()

sc = SparkContext("local", "test")

