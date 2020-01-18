import io
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()

about = {}
with io.open(
    os.path.join(here, "tutorsaml", "__about__.py"),
    "rt",
    encoding="utf-8",
) as f:
    exec(f.read(), about)

setup(
    name="tutor-saml",
    version=about["__version__"],
    url="https://github.com/pdebruic/tutor-saml",
    project_urls={
        "Code": "https://github.com/pdebruic/tutor-saml",
        "Issue tracker": "https://github.com/pdebruic/tutor-saml/issues",
    },
    license="AGPLv3",
    author="Paul DeBruicker",
    description="saml plugin for Tutor",
    long_description=readme,
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=["tutor-openedx"],
    entry_points={
        "tutor.plugin.v0": [
            "saml = tutorsaml.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
