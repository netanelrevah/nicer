import time

from nicer.times import Timestamp


def test_timestamp_lt():
    assert not Timestamp(1, 0) < Timestamp(1, 0)

    assert Timestamp(1, 0) < Timestamp(2, 0)
    assert not Timestamp(2, 0) < Timestamp(1, 0)

    assert Timestamp(1, 0) < Timestamp(1, 1)
    assert not Timestamp(1, 1) < Timestamp(1, 0)


def test_timestamp_gt():
    assert not Timestamp(1, 0) > Timestamp(1, 0)

    assert Timestamp(2, 0) > Timestamp(1, 0)
    assert not Timestamp(1, 0) > Timestamp(2, 0)

    assert Timestamp(1, 1) > Timestamp(1, 0)
    assert not Timestamp(1, 0) > Timestamp(1, 1)


def test_timestamp_ge():
    assert Timestamp(1, 0) >= Timestamp(1, 0)

    assert Timestamp(2, 0) >= Timestamp(1, 0)
    assert not Timestamp(1, 0) >= Timestamp(2, 0)

    assert Timestamp(1, 1) >= Timestamp(1, 0)
    assert not Timestamp(1, 0) >= Timestamp(1, 1)


def test_timestamp_le():
    assert Timestamp(1, 0) <= Timestamp(1, 0)

    assert Timestamp(1, 0) <= Timestamp(2, 0)
    assert not Timestamp(2, 0) <= Timestamp(1, 0)

    assert Timestamp(1, 0) <= Timestamp(1, 1)
    assert not Timestamp(1, 1) <= Timestamp(1, 0)


def test_timestamp_eq():
    assert Timestamp(1, 0) == Timestamp(1, 0)
    assert not Timestamp(2, 0) == Timestamp(1, 0)

    assert Timestamp(1, 0) != Timestamp(2, 0)

    assert Timestamp(1, 1) == Timestamp(1, 1)
    assert Timestamp(1, 1) != Timestamp(1, 0)


def test_timestamp_now():
    for i in range(100):
        before = Timestamp.from_timestamp(time.time(), precision=i)
        now = Timestamp.now(i)
        after = Timestamp.from_timestamp(time.time(), precision=i)

        assert before <= now <= after
