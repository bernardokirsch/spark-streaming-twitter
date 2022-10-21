from pyspark.sql import SparkSession
from pyspark.sql import functions as f

spark = SparkSession.builder.appName('SparkStreaming').getOrCreate()

lines = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9008)\
    .load()

words = lines.select(f.explode(f.split(lines.value, ' ')).alias('Word'))

words_count = words.groupBy('Word').count()

query = words_count.writeStream\
    .outputMode('complete')\
    .format('console')\
    .start()

query.awaitTermination()