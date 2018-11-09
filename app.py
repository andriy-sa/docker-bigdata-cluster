import os

from pyspark.sql import SparkSession

sc = SparkSession \
    .builder \
    .config("spark.executor.memory", "1g") \
    .config("spark.cores.max", "2") \
    .appName("test_rdd") \
    .getOrCreate()

if __name__ == '__main__':
    text_file = sc.read.text("hdfs://namenode:9000/user/hdfs/test_text.txt").rdd

    rdd = text_file.flatMap(lambda line: line.value.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortBy(lambda x: x[1], False)

    df = sc.createDataFrame(rdd, ['word', 'count'])
    df.show()
