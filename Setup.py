from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'A simple math quiz project'

# Setting up
setup(
    name="mathquiz",
    version=VERSION,
    author="Sajid Akhtar",
    author_email="<sajid.akhtar9823@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'math', 'math-quiz',
              'assignment', 'ml'],
    classifiers=[
        "Development Status :: 1 - Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
