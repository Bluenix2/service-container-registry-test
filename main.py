import os

print(os.environ)

try:
  with open(os.environ['GITHUB_ENV'], 'a') as f:
    f.write('EXECUTED_PYTHON=true')
except Exception as e:
  print(e)
