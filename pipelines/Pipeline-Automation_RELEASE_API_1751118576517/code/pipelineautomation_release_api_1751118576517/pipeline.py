from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipelineautomation_release_api_1751118576517.config.ConfigStore import *
from pipelineautomation_release_api_1751118576517.functions import *
from prophecy.utils import *
from pipelineautomation_release_api_1751118576517.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Project_Automation_python_RELEASE_API_1751118576517_dataSet = Project_Automation_python_RELEASE_API_1751118576517_dataSet(
        spark
    )
    df_select_customer_details = select_customer_details(
        spark, 
        df_Project_Automation_python_RELEASE_API_1751118576517_dataSet
    )

def main():
    spark = SparkSession.builder\
                .enableHiveSupport()\
                .appName("Pipeline-Automation_RELEASE_API_1751118576517")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pipeline-Automation_RELEASE_API_1751118576517")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(
        spark = spark,
        pipelineId = "pipelines/Pipeline-Automation_RELEASE_API_1751118576517",
        config = Config
    )(
        pipeline
    )

if __name__ == "__main__":
    main()
