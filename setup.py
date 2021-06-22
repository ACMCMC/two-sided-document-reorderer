from setuptools import setup

setup(
   name='Two-Sided Document Reorderer',
   version='0.1.2',
   author='Aldán Creo',
   author_email='aldan.creo@gmail.com',
   packages=['two_sided_document_reorderer'],
   url='https://github.com/ACMCMC/two-sided-document-reorderer',
   license='',
   description='A Python package that reorders two PDF documents (corresponding to two sides of a single document) and shuffles the pages to create a single in-order document',
   long_description=open('README.md').read(),
   install_requires=[
       'PyPDF2',
       'pytest',
   ],
)
