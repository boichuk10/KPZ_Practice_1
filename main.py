from lab2 import prime_num_generator
from lab3 import palindrom
from lab3 import validate_ip
from lab3 import get_os


def test_firsr_twelve_primes():
    generator = prime_num_generator()
    first = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for i in range(9):
        assert next(generator) == first[i]

    generator_one = prime_num_generator()
    for i in range(100):
        next(generator_one)
    assert next(generator_one) == 547


def test_get_os():
    assert get_os() == 'Windows'


def test_validate_ip():
    faker = Faker()
    for i in range(50):
        assert validate_ip(faker.ipv4()) == True
    assert False == validate_ip("0.444.0.0")

    with pytest.raises(Exception):
        assert False == validate_ip('2.0.0')
    with pytest.raises(Exception):
        assert False(123)
    assert isinstance(validate_ip(faker.ipv4(), bool)) == True


def test_palindrom():
    with pytest.raises(TypeError):
        palindrom()
    with pytest.raises(TypeError):
        palindrom(123)
    assert palindrom('Hello world') == []
    assert palindrom("BOOS, HONDA, BIBI, LIKE") == ['BOOS', 'BIBI']