from distutils.core import setup
from profitshare import __version__ as VERSION

setup(name='profitshare',
      version=VERSION,
      description='ProfitShare API wrapper',
      packages=['profitshare'],
      requires=['requests'],
)
