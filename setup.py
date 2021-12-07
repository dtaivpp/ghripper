from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ghripper",
    version='0.0.1',
    author="David Tippett",
    description="A tool for replacing and committing text from all repos in a certain scope",
    license='Apache Software License',
    license_files=['LICENSE'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="GitHub Replacement Automated Commit",
    url="https://github.com/dtaivpp/ghripper",
    packages=['ghripper'],
    install_requires=['ghapi','python-dotenv', 'wheel'],
    entry_points = {
        'console_scripts': ['ghripper=ghripper.ripper:cli_entry'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        'Intended Audience :: Developers',
        "Operating System :: OS Independent"
    ],
)
