from setuptools import setup, find_packages
setup(
    name = 'Pipeline-Automation_RELEASE_API_1739174606426',
    version = '1.0',
    packages = (
      find_packages(include = ('pipelineautomation_release_api_1739174606426*', ))
      + ['prophecy_config_instances.pipelineautomation_release_api_1739174606426']
    ),
    package_dir = {
      'prophecy_config_instances.pipelineautomation_release_api_1739174606426': 'configs/resources/pipelineautomation_release_api_1739174606426'
    },
    package_data = {'prophecy_config_instances.pipelineautomation_release_api_1739174606426' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.33'],
    entry_points = {
'console_scripts' : [
'main = pipelineautomation_release_api_1739174606426.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
