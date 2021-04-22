import sys
sys.argv = ['manage.py', 'test', 'catalog.tests.test_models']
exec(open('manage.py').read())

