from __future__ import absolute_import

import re

from .utils import validator

pattern = re.compile(r'\d\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d*')


@validator
def orcid(value):
    """
    Return whether or not given value is a valid ORCID.

    If the value is valid ORCID this function returns ``True``, otherwise
    :class:`~validators.utils.ValidationFailure`.

    Examples::

        >>> orcid('0000-0003-4401-6496')
        True

        >>> orcid('2bc1c94f 0deb-43e9-92a1-4775189ec9f8')
        ValidationFailure(func=orcid, ...)

    .. versionadded:: 0.18.3

    :param value: ORCID value to validate
    """
    try:
        return pattern.match(value)
    except TypeError:
        return False
