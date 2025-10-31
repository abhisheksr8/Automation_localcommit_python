from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from automation_localcommit_python_pipeline.config.ConfigStore import *
from automation_localcommit_python_pipeline.functions import *
from prophecy.utils import *
from automation_localcommit_python_pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_test_dataset = test_dataset(spark)
    df_compose_config_column = compose_config_column(spark, df_test_dataset)

def main():
    spark = SparkSession.builder\
                .enableHiveSupport()\
                .appName("Automation_localcommit_python_Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Automation_localcommit_python_Pipeline")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(
        spark = spark,
        pipelineId = "pipelines/Automation_localcommit_python_Pipeline",
        config = Config
    )(
        pipeline
    )

if __name__ == "__main__":
    main()
