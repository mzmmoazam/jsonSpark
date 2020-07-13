# JsonSpark

This package is meant to give a python simplicity and feel to pyspark while handling json files.

It is very simple to use and doesn't need extra information if you are using python.

# Installation
`pip install jsonSpark`

# Sample Usage:
* Import the package<Br>
    `
    import jsonSpark
    `
* Pass the pyspark json file object<br>
`
df = sql.read.json("filename", multiLine=True) # or get from S3 bucket
`
* Create a JsonSpark object.<br>
`
df = jsonSpark(df)
`
* See the schema if you wish.<br>
`
df.printSchema()
`
* Display the Data<br>
`
df.show()
`
* Use it as python dictionary<br>
`
df["key1"]["key2"]["key3"]["key4"].show()
`

* You can use the pyspark functions by converting the object back to pyspark object.<br>
`
pysparkObject = df._toDF()
`
### I will update the documentation and include a working example soon .... 
