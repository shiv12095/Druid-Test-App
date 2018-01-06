from setuptools import setup

setup(
    name='drask',
    packages=['drask'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pydruid'
    ],
)
