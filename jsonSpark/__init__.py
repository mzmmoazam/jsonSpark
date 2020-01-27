import pyspark as spark
from pyspark.sql.utils import AnalysisException
from pyspark.sql import functions as F


class jsonSpark:
    '''
    author : mzm >> https://github.com/mzmmoazam/
    Connect and Say Hi on >> https://www.linkedin.com/in/mzmmoazam
    '''

    def __init__(self, dataframe):
        if not isinstance(dataframe, spark.sql.dataframe.DataFrame):
            raise Exception("dataframe not an instance of spark.sql.dataframe.DataFrame")
        self.df = dataframe

    def _has_column(self, column_name):
        try:
            self.df[column_name]
            return True
        except AnalysisException:
            return False

    def mergeToOrigin(self,column_name):
        # .extend([col for col in self.df.columns if col != column_name])
        # return self.df.select([f"{column_name}.*"])
        return jsonSpark(self.df.select([f"{column_name}.*"]+[col for col in self.df.columns if col != column_name]))

    def __getitem__(self, column_name):
        if self._has_column(column_name):
            if len(self.df.columns) > 1:
                try:
                    tmp = self.df.withColumn(column_name, F.explode(column_name))
                except Exception as e:
                    tmp = self.df
                try:
                    tmp = tmp.select(f"{column_name}.*")
                except Exception as e:
                    tmp = self.df.select([column_name])

            else:
                tmp = self.df.select(column_name)

            return jsonSpark(tmp)

        else:
            raise Exception(f"Column {column_name} not found")

    def where(self, column_name, operator, value,valueRegrex=False):
        if operator != operators.regrex_search:
            if isinstance(value, str):
                eval_str = f"F.col('{column_name}') {operator} '{value}'"
            else:
                eval_str = f"F.col('{column_name}') {operator} {value}"
            tmp = self.df.where(eval(eval_str))
            return jsonSpark(tmp)
        else:
            return jsonSpark(self.df.filter(self.df[column_name].rlike(value)))

    def show(self):
        self.df.show()

    def printSchema(self):
        self.df.printSchema()

    def _toDF(self):
        return self.df




class operators:
    equal_to = "=="
    less_than = "<"
    greater_than = ">"
    less_than_equal_to = "<="
    greater_than_equal_to = ">="
    regrex_search = "rlike"

