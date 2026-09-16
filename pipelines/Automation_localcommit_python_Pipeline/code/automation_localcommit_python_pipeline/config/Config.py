from prophecy.config import ConfigBase


class C_record(ConfigBase):
    def __init__(
            self,
            prophecy_spark=None,
            c_string: str="this is my123string sama",
            c_boolean: bool=False,
            c_float: float=-23.34,
            **kwargs
    ):
        self.c_string = c_string
        self.c_boolean = c_boolean
        self.c_float = c_float
        pass


class Config(ConfigBase):

    def __init__(self, c_array: list=None, c_int_basic: int=None, c_record: dict=None, **kwargs):
        self.spark = None
        self.update(c_array, c_int_basic, c_record)

    def update(self, c_array: list=[10, 20, 100, -10, 0, 20], c_int_basic: int=-65530, c_record: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.c_array = c_array
        self.c_int_basic = self.get_int_value(c_int_basic)
        self.c_record = self.get_config_object(
            prophecy_spark, 
            C_record(prophecy_spark = prophecy_spark), 
            c_record, 
            C_record
        )
        pass
