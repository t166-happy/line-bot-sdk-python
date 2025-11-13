# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

"""linebot.v3.utils module."""


import logging
import re

import sys

LOGGER = logging.getLogger('linebot')

PY3 = sys.version_info[0] == 3


def to_snake_case(text):
    """Convert to snake case.

    :param str text:
    :rtype: str
    """
    s1 = re.sub('(.)([A-Z])', r'\1_\2', text)
    s2 = re.sub('(.)([0-9]+)', r'\1_\2', s1)
    s3 = re.sub('([0-9])([a-z])', r'\1_\2', s2)
    return s3.lower()


def to_camel_case(text):
    """Convert to camel case.

    :param str text:
    :rtype: str
    """
    split = text.split('_')
    return split[0] + "".join(x.title() for x in split[1:])


def safe_compare_digest(val1, val2):
    """Return ``True`` if the two strings are equal, ``False`` otherwise.

    As with :func:`hmac.compare_digest`, both inputs must be of the same type.
    In previous versions mixing ``str`` and ``bytes`` would result in a
    ``TypeError`` from :func:`ord`.  The function now explicitly checks the
    types and raises ``TypeError`` when they don't match.

    :param val1: First value for comparison.
    :type val1: str | bytes
    :param val2: Second value for comparison.
    :type val2: str | bytes
    """

    if type(val1) is not type(val2):
        raise TypeError('Inputs must be of the same type')

    if len(val1) != len(val2):
        return False

    result = 0
    if PY3 and isinstance(val1, bytes):
        for i, j in zip(val1, val2):
            result |= i ^ j
    else:
        for i, j in zip(val1, val2):
            result |= (ord(i) ^ ord(j))

    return result == 0
