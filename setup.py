from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rfq_fix/__init__.py
from rfq_fix import __version__ as version

setup(
	name="rfq_fix",
	version=version,
	description="fix for rfq webform",
	author="Nigmacorp",
	author_email="tripleo4u@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
