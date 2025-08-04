from setuptools import setup, find_packages
setup(
    name = 'Automation_localcommit_python_Pipeline',
    version = '1.0',
    packages = (
      find_packages(include = ('automation_localcommit_python_pipeline*', ))
      + ['prophecy_config_instances.automation_localcommit_python_pipeline']
    ),
    package_dir = {
      'prophecy_config_instances.automation_localcommit_python_pipeline': 'configs/resources/automation_localcommit_python_pipeline'
    },
    package_data = {'prophecy_config_instances.automation_localcommit_python_pipeline' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.1'],
    entry_points = {
'console_scripts' : [
'main = automation_localcommit_python_pipeline.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
