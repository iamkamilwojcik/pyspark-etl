from base.driver import driver

spark_driver = driver(app_name='my_app')
spark_session = spark_driver.spark_start()

def extract():
    df = spark_session.read.csv(path="data/FL_insurance_sample.csv", inferSchema=True, sep=",")
    print(df.show(20))

extract()