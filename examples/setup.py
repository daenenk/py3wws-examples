import setuptools

setuptools.setup(
    name="py3wws_examples",
    version="1.0.0",
    author="Anton Dries",
    author_email="anton.dries@nokia-bell-labs.com",
    description="A library of WWS operators that demonstrate the py3wws.wrap library.",
    url="https://nok.it/wws-docs/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=['py3wws'],
    python_requires='>=3.8'
)
