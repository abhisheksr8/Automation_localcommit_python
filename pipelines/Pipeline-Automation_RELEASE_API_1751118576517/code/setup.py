from setuptools import setup, find_packages
setup(
    name = 'Pipeline-Automation_RELEASE_API_1751118576517',
    version = '1.0',
    packages = (
      find_packages(include = ('pipelineautomation_release_api_1751118576517*', ))
      + ['prophecy_config_instances.pipelineautomation_release_api_1751118576517']
    ),
    package_dir = {
      'prophecy_config_instances.pipelineautomation_release_api_1751118576517': 'configs/resources/pipelineautomation_release_api_1751118576517'
    },
    package_data = {'prophecy_config_instances.pipelineautomation_release_api_1751118576517' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.3'],
    entry_points = {
'console_scripts' : [
'main = pipelineautomation_release_api_1751118576517.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
