from setuptools import setup, find_packages

with open("requirements.txt") as f:
      install_requires = f.read().strip().split("\n")

from jb_core_app import __version__ as version

setup(
      name="jb_core_app",
      version=version,
      description="JB Core App - Phase R shared server and client script estate for jh",
      author="JB Grocers LLP",
      author_email="sachingoel24@gmail.com",
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      install_requires=install_requires
)
