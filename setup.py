from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sale_barcode_printing/__init__.py
from sale_barcode_printing import __version__ as version

setup(
	name="sale_barcode_printing",
	version=version,
	description="This app will give a feature to print sale barcode.",
	author="Kanak Infosystems LLP",
	author_email="sales@kanakinfosystems.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
