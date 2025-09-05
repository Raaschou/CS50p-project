import pytest
from project import parse_date

def main():
    ...


def test_parse_date():
    assert parse_date("12/10/2019") == "2019-12-10"


if __name__ == "__main__":
    main()
