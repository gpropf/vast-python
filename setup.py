from setuptools import setup

 setup(
   name='vast-cli',
   version='0.1.0',
   author='Vast Inc.',
   author_email='gpropf@gmail.com',
   packages=['vast-cli'],
   scripts=['bin/vast.py','bin/vast_pdf.py','bin/make_command_docs.py'],
   url='http://vast.ai',
   license='LICENSE.txt',
   description='CLI interface to the Vast system.',
   long_description=open('README.md').read(),
   install_requires=[
       "borb==2.0.17",
       "Cython==0.29.28",
       "Pillow==8.4.0",
       "requests==2.27.1",
       "requests-unixsocket==0.1.5",
       "simplejson==3.13.2"
   ],
)