from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from automation_localcommit_python_pipeline.config.ConfigStore import *
from automation_localcommit_python_pipeline.udfs.UDFs import *

def config_column_reformat(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        concat(lit(Config.c_int_basic), lit(Config.c_record.c_string), lit(Config.c_array[0])).alias("c_config_col")
    )
