from setuptools import setup, find_packages

requirements = [
    "requests",
    "websocket-client==1.3.1", 
    "setuptools", 
    "json_minify", 
    "six",
    "aiohttp",
    "websockets"
]

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name="amino.cx",
    license="MIT",
    author="Victorcx",
    version="1.0",
    author_email="suppport.time.amino@gmail.com	",
    description="Library for Amino. Discord - https://discord.gg/Bf3dpBRJHj",
    url="https://github.com/cxvictor/Amino.cx",
    packages=find_packages(),
    long_description=long_description,
    install_requires=requirements,
    keywords=[
        'aminoapps',
        'amino.fix',
        'amino',
        'amino.cx',
        'amino-bot',
        'narvii',
        'api',
        'python',
        'python3',
        'python3.x',
        'minori',
        'eozak',
        'victorcx'
    ],
    python_requires='>=3.6',
)
