import pytest
import _pytest

FIXTURES_SEEN = set()
FIXTURE_MANAGER_PATCHED = False


def pytest_plugin_registered(plugin):
    global FIXTURE_MANAGER_PATCHED
    if not FIXTURE_MANAGER_PATCHED:
        orig = _pytest.fixtures.FixtureDef.__init__

        def init_wrapper(*args, argname, func, **kwargs):
            if argname in FIXTURES_SEEN:
                if not any(
                    mark.name == "dupe" for mark in getattr(func, "pytestmark", [])
                ):
                    pytest.fail(f"""Duplicate fixture {argname!r} found!
        If this is intended, mark the overriding fixture with pytest.mark.dupe.""")
            FIXTURES_SEEN.add(argname)
            return orig(*args, argname=argname, func=func, **kwargs)

        _pytest.fixtures.FixtureDef.__init__ = init_wrapper
        FIXTURE_MANAGER_PATCHED = True


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "dupe: allow fixture to be able to override an existing fixture of the same name",
    )
