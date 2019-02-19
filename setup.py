import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tkintertoy",
    version="1.0.0",
    author="Mike Callahan",
    author_email="mcalla@twc.com",
    description="A simple GUI package based on Tkinter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=[tkintertoy],
    keywords=['GUI','Tkinter'],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces"
    ],
)