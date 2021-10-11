import os.path
import setuptools

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'README.md'), 'r') as fh:
    README = fh.read()

setuptools.setup(
    name='text-message-sender',
    version='0.0.1',
    author='Jeff Martin',
    author_email='jeffrey.j.martin2@gmail.com',
    description='Send one-off or recurring text messages',
    long_description=README,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/theletterjeff/text-message-sender',
    classifiers={
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    },
    packages=setuptools.find_packages(include=['text_message_sender', 'text_message_sender.*']),
    python_requires='>=3.6',
    install_requires=[
        'pandas>=1.1.1',
        'python-dotenv>=0.19.0',
    ]
)