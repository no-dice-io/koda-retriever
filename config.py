"""
Imports and code below are only necessary for testing and demo purposes (notebooks).

This has no impact on the source code itself. Although feel free to use it in your own projects.
"""

from dynaconf import Dynaconf

settings = Dynaconf(
    # export envvars with `export KODA_FOO=bar`, then access with `settings.foo`
    envvar_prefix="KODA"
)
