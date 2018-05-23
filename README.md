## Hister - a command line browser history tool

Hister lets you easily capture, search, and reopen links from your browser's current session and history from the command line

Example usage:

```
$ hister save
Saved 4 new documents:
  - 1fe7c0 [Welcome to the Click Documentation — Click Documentation (6.0)](http://click.pocoo.org/6/)
  - ed35d1 [Introduction — PyObjC - the Python to Objective-C bridge](http://pyobjc.readthedocs.io/en/latest/)
  - d889d7 [Immersive Math](http://immersivemath.com/ila/index.html)
  - 5e630f [Pipenv: Python Dev Workflow for Humans — pipenv 2018.05.18 documentation](https://docs.pipenv.org/)
$ hister search python
Found 2 documents:
  - ed35d1 [Introduction — PyObjC - the Python to Objective-C bridge](http://pyobjc.readthedocs.io/en/latest/)
  - 5e630f [Pipenv: Python Dev Workflow for Humans — pipenv 2018.05.18 documentation](https://docs.pipenv.org/)
$ hister rm ed35d1
Removed 1 document:
  - ed35d1 [Introduction — PyObjC - the Python to Objective-C bridge](http://pyobjc.readthedocs.io/en/latest/)
$ hister list today
Found 3 documents from today:
  - 1fe7c0 [Welcome to the Click Documentation — Click Documentation (6.0)](http://click.pocoo.org/6/)
  - d889d7 [Immersive Math](http://immersivemath.com/ila/index.html)
  - 5e630f [Pipenv: Python Dev Workflow for Humans — pipenv 2018.05.18 documentation](https://docs.pipenv.org/)
```
