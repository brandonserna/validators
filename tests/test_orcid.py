# -*- coding: utf-8 -*-
import pytest

from validators import orcid, ValidationFailure


@pytest.mark.parametrize(('id',), [
    ('0000-0003-4401-6496',),
    ('0000-0003-4401-6496',),
])
def test_returns_true_on_valid_orcid(id):
    assert orcid(id)


@pytest.mark.parametrize(('id',), [
    ('0000-00ddddd03-4401-6496',),
    ('      0000-0003-4401-6496',),
])
def test_returns_failed_validation_on_invalid_orcid(id):
    assert isinstance(orcid(id), ValidationFailure)
