from setuptools import setup, find_packages


with open("ReadMe.md", 'r') as f:
    long_description = f.read()

setup(
    name='word_geni.py',
    version='1.0',
    author='Cherloy',
    author_email='sideswipe8@mail.ru',
    description='generate word file with random data',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url='https://github.com/Cherloy/Word_gen',
    packages = find_packages(),
    license='MIT',
    test_suite='tests',
    python_requires='>=3.6'
)
