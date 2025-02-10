from setuptools import setup, find_packages
packages_to_include = find_packages(exclude = ['test.*', 'test', 'test_manual'])
setup(
    name = 'abhishekse2etestsprophecyioteam_projectautomationpythonreleaseapi1739174606426',
    version = '17391746064261.0.0',
    packages = packages_to_include,
    description = '',
    install_requires = [],
    data_files = ["resources/extensions.idx"]
)
