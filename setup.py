from distutils.core import setup

with open('README') as file:
    readme = file.read()
    
setup(         
      name='WarGame_OrcsAttack',
      version='2.0.0',
      packages=['wargame'],
      licence='LICENCE.txt',
      description='my fantasy ORC game',
      long_description=readme,
      author='Tuna ERTEKIN',
      author_email='tunaertekin@gmail.com'
)