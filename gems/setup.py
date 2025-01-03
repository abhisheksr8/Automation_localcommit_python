from setuptools import setup, find_packages
packages_to_include = find_packages(exclude = ['test.*', 'test', 'test_manual'])
setup(
    name = 'abhishekse2etestsprophecyioteam_projectautomationpythonreleaseapi1735891051639',
    version = '17358910516391.0.0',
    packages = packages_to_include,
    description = '',
    install_requires = [],
    data_files = ["resources/extensions.idx"]
)
