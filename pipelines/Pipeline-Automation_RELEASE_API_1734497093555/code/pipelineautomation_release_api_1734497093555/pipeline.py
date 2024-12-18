from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipelineautomation_release_api_1734497093555.config.ConfigStore import *
from pipelineautomation_release_api_1734497093555.functions import *
from prophecy.utils import *
from pipelineautomation_release_api_1734497093555.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Project_Automation_python_RELEASE_API_1734497093555_dataSet = Project_Automation_python_RELEASE_API_1734497093555_dataSet(
        spark
    )
    df_customer_details_selection = customer_details_selection(
        spark, 
        df_Project_Automation_python_RELEASE_API_1734497093555_dataSet
    )

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Pipeline-Automation_RELEASE_API_1734497093555")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pipeline-Automation_RELEASE_API_1734497093555")
    registerUDFs(spark)
    
    MetricsCollector.instrument(
        spark = spark,
        pipelineId = "pipelines/Pipeline-Automation_RELEASE_API_1734497093555",
        config = Config
    )(
        pipeline
    )

if __name__ == "__main__":
    main()
