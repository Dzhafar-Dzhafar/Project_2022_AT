import pytest
import time


@pytest.fixture(scope="module")
def resource_setup(request):
    print("\nconnect to DB")
    db: dict[str, int] = {'Red': 1,
                          "Blue": 2,
                          "Green": 3}

    def resource_teardown():
        print("\ndisconnect")

    request.addfinalizer(resource_teardown)
    return db

def test_db(resource_setup):
    for k in resource_setup.keys():
        print('color {0} has id {1}'.format(k, resource_setup[k]))


def test_red(resource_setup):
    assert resource_setup["Red"]==1

def test_blue(resource_setup):
    assert resource_setup["Blue"] !=1

@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Сообщает время в конце session(сеанса)."""
    yield
    now = time.time()
    print('--')
    print('finished : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')

@pytest.fixture(autouse=True)
def footer_function_scope():
    """Сообщает продолжительность теста после каждой функции."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.3} seconds'.format(delta))

def test_1():
    time.sleep(3)

def test_2():
    time.sleep(4.23)