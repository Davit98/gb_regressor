from pathlib import Path

from setuptools import find_packages, setup

# package metadata
NAME = 'gb_regressor'
DESCRIPTION = "Gradient boosting regression model for performing house price predictions."
URL = "https://github.com/Davit98/gb_regressor"
EMAIL = "dvmartirosyan@gmail.com"
AUTHOR = "Davit98"
REQUIRES_PYTHON = ">=3.8.0"


# what packages are required for this module to be executed?
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

# load the package's VERSION file as a dictionary.
about = {}
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / 'gb_regressor'
with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version


# this is where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=["gb_regressor"],
    package_data={"gb_regressor": ["VERSION"]},
    install_requires=requirements,
    extras_require={},
    include_package_data=True,
    license="MIT"
)
