from setuptools import find_packages, setup

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst', 'md')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='huobi',
    version='0.1.11',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    license='MIT License',
    description='Huobi Python SDK',
    long_description=long_description,
    url='https://github.com/ericls/huobi',
    author='Shen Li',
    author_email='dustet@gmail.com',
    install_requires=[
        "requests>=2.4.2",
        "aiohttp>=3.1.0",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
