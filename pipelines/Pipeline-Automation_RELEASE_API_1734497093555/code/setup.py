from setuptools import setup, find_packages
setup(
    name = 'Pipeline-Automation_RELEASE_API_1734497093555',
    version = '1.0',
    packages = find_packages(include = ('pipelineautomation_release_api_1734497093555*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.28'],
    entry_points = {
'console_scripts' : [
'main = pipelineautomation_release_api_1734497093555.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
