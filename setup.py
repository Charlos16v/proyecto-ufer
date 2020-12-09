import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UFER_Scrapping_TOOL",
    version="0.0.1",
    author="Carlos Uriel Dominguez Ruiz Diaz y Juan Pastor Ruiz Molina",
    author_email="cdominguez@cifpfbmoll.eu jruiz@cifpfbmoll.eu",
    description="A small tool for scrapp websites.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Charlos16v/proyecto-ufer/",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests==2.25.0',
        'pymongo==3.11.2',
        'dnspython==2.0.0',
    ],
)