# pytest-fixture-rtttg

_In the face of ambiguity, refuse the temptation to guess._

This plugin detects when you have two fixtures that share the same name, and
throws an error in that case, instead of silently choosing the later/inner-most
one.


## Installation

    pip install pytest-fixture-rtttg

After this, the plugin should automatically do its job.

## Customization

When the duplicate name is intentional, you can use the `dupe` mark to stop
this from happening:

```py
@pytest.fixture
@pytest.mark.dupe
def some_fixture():
    ...
```

Usually though, you're better of just choosing a different name.
