import pytest
from http import HTTPStatus
from models.ipapi import IpApi


@pytest.mark.parametrize('data, status', [('8.8.8.8', 'United States'),
                                          ('195.160.232.254', 'Ukraine'),
                                          ('176.156.59.89', 'France'),
                                          ('176.1.9.8', 'Germany'),
                                          ('8', 'Undefined'),
                                          ('ad', 'Undefined'),
                                          ('', 'Ukraine')
                                          ])
def test_get_country(data, status):
    assert IpApi().get_country(data).text == status


@pytest.mark.parametrize('data, status', [('!', HTTPStatus.NOT_FOUND),
                                          ('оро', HTTPStatus.NOT_FOUND),
                                          ])
def test_get_country_wrong(data, status):
    assert IpApi().get_country(data).status_code == status


@pytest.mark.parametrize('data, status', [('8.8.8.8', 'Mountain View'),
                                          ('195.160.232.254', 'Lviv'),
                                          ('176.156.59.89', 'Toulouse'),
                                          ('176.1.9.8', 'Frankfurt am Main'),
                                          ('8', 'Undefined'),
                                          ('ad', 'Undefined'),
                                          ('', 'Lviv')
                                          ])
def test_get_city(data, status):
    assert IpApi().get_city(data).text == status


@pytest.mark.parametrize('data, status', [('!', HTTPStatus.NOT_FOUND),
                                          ('оро', HTTPStatus.NOT_FOUND),
                                          ])
def test_get_city_wrong(data, status):
    assert IpApi().get_city(data).status_code == status


@pytest.mark.parametrize('data, status', [('8.8.8.8', 'Google LLC'),
                                          ('195.160.232.254', 'SoftServe Ltd.'),
                                          ('176.156.59.89', 'Bouygues Telecom SA'),
                                          ('176.1.9.8', 'Telefonica Germany'),
                                          ('8', 'Undefined'),
                                          ('ad', 'Undefined'),
                                          ('', 'SoftServe Ltd.')
                                          ])
def test_get_organizations(data, status):
    assert IpApi().get_organizations(data).text == status


@pytest.mark.parametrize('data, status', [('!', HTTPStatus.NOT_FOUND),
                                          ('оро', HTTPStatus.NOT_FOUND),
                                          ])
def test_get_organizations_wrong(data, status):
    assert IpApi().get_organizations(data).status_code == status


@pytest.mark.parametrize('data, status', [('8.8.8.8', 'USD'),
                                          ('195.160.232.254', 'UAH'),
                                          ('176.156.59.89', 'EUR'),
                                          ('176.1.9.8', 'EUR'),
                                          ('8', 'Undefined'),
                                          ('ad', 'Undefined'),
                                          ('', 'UAH')
                                          ])
def test_get_currency(data, status):
    assert IpApi().get_currency(data).text == status


@pytest.mark.parametrize('data, status', [('!', HTTPStatus.NOT_FOUND),
                                          ('оро', HTTPStatus.NOT_FOUND),
                                          ])
def test_get_currency_wrong(data, status):
    assert IpApi().get_currency(data).status_code == status

