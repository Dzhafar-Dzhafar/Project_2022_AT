import pytest
import time


@pytest.fixture(scope="module")
def resource_setup(request):
    print("\nconnect to DB")
    db: dict[str, int] = {'name1': 1,
                          "name2": 2,
                          "name3": 3}

    def resource_teardown():
        print("\ndisconnect")

    request.addfinalizer(resource_teardown)
    return db


def test_db(resource_setup):
    for k in resource_setup.keys():
        print('name {0} has id {1}'.format(k, resource_setup[k]))


def test_red(resource_setup):
    assert resource_setup["name1"] == 1


def test_blue(resource_setup):
    assert resource_setup["name2"] != 1


def test_green(resource_setup):
    assert resource_setup["name3"] == 3


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Сообщает время в конце сеанса"""
    yield
    now = time.time()
    print('--')
    print('finished : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Сообщает продолжительность теста после каждой функции"""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.3} seconds'.format(delta))


def test_1() -> None:
    time.sleep(3)


def test_2() -> None:
    time.sleep(4.23)
