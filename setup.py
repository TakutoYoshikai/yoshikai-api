from setuptools import setup, find_packages

setup(
    name = 'yoshikai',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/yoshikai-api.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = "This is a library to fetch Takuto Yoshikai's portfolio data.",
    install_requires = ['setuptools', "beautifulsoup4"],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
        ]
    }
)
