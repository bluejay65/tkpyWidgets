import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="tkpywidgets",
    version=0.1,
    author="Jack Horvath",
    author_email="jmhorvath65@gmail.com",
    description="A library of more advanced widgets for tkinter made in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.cm/bluejay65/tkpyWidgets",
    packages=setuptools.find_packages(),
    license='MIT License',
    install_requires=['tk'],
    keywords='tkinter',
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
