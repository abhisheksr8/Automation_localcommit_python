from setuptools import setup, find_packages
setup(
    name = 'Pipeline-Automation_RELEASE_API_1746215421424',
    version = '1.0',
    packages = (
      find_packages(include = ('pipelineautomation_release_api_1746215421424*', ))
      + ['prophecy_config_instances.pipelineautomation_release_api_1746215421424']
    ),
    package_dir = {
      'prophecy_config_instances.pipelineautomation_release_api_1746215421424': 'configs/resources/pipelineautomation_release_api_1746215421424'
    },
    package_data = {'prophecy_config_instances.pipelineautomation_release_api_1746215421424' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.49'],
    entry_points = {
'console_scripts' : [
'main = pipelineautomation_release_api_1746215421424.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
