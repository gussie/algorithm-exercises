


def test_can_put_and_get():
    d = Di()
    d.put(1, "one")
    assert d.get(1) == "one"

def test_can_overwrite():
    d = Di()
    d.put(1, "one")
    d.put(1, "one - new")
    assert d.get(1) == "one - new"

def test_can_delete_random():
    d = Di()
    d.put(1, "one")

    assert d.delete_random() == (1, "one")

def test_can_handle_much_data():
    d = Di()
    for i in range(100):
        d.put(1, str(1))