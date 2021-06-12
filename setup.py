import setuptools

with open("ReadMe.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='word_gener',
    version='1.1',
    author='Cherloy',
    author_email='sideswipe8@mail.ru',
    description='generate word file with random data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Cherloy/Word_gen',
    packages=setuptools.find_packages(),
    license='MIT',
    test_suite='tests',
    python_requires='>=3.6'
)