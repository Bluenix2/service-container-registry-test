import os

print(os.environ)

with open(os.environ['GITHUB_ENV'], 'a') as f:
  f.write('EXECUTED_PYTHON=true')
