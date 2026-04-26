import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="headlessdomains",
    version="0.1.4",
    author="Headless Domains",
    author_email="hello@headlessdomains.com",
    description="Official Python SDK for the Headless Domains API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shadstoneofficial/headlessdomains-python-sdk",
    project_urls={
        "Bug Tracker": "https://github.com/shadstoneofficial/headlessdomains-python-sdk/issues",
        "Documentation": "https://docs.headlessdomains.com/api/python-sdk",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.7",
    install_requires=[
        "httpx>=0.24.0",
        "pydantic>=2.0.0",
    ],
)
