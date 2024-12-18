from setuptools import setup, find_packages

setup(
    name="grid-trader",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "alpaca-trade-api==2.3.0",
        "rich==12.5.1",
        "aiohttp==3.7.4",
        "pandas==1.5.3",
        "numpy==1.24.3",
        "websockets==10.4",
        "PyYAML==6.0",
    ],
    python_requires=">=3.9,<3.10",
) 