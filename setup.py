import setuptools

# with open('README.md', 'r') as fh:
#     long_description = fh.read()

setuptools.setup(
    name='myhello',
    version='0.1',
    description='A helloworld package',
    url='https://github.com/jiho/myhello',
    author='jiho',
    author_email='jo.irisson@gmail.com',
    license='GPL3',
    # long_description=long_description,
    # long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    scripts=['bin/myhello'],
    # packages=['myhello'],
    python_requires='>=3.6'
)