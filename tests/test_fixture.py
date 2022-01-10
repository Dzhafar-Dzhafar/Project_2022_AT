def test_fixture_property(show_affiliation):
    assert 1 == 1


def test_fixture_property_2(show_affiliation):
    assert [1, 2, 3] != [3, 2, 1]
    if [1, 2, 3] == [3, 2, 1]:
        print("ERROR: [1, 2, 3] не равно [3, 2, 1]")
