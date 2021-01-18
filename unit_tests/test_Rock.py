from rock.Rock import Rock

# def test_claster():
#     rock = Rock(data=[3, 4, 5, 10], eps=4, number_of_clasters=2 )
#     rock.cluster([3, 4, 5, 10], 2)
#     assert True
def test_claster():
    rock = Rock(data=[3, 5, 8, 9], eps=4, number_of_clasters=2 )
    rock.cluster([3, 5, 8, 9], 2)
    assert True

# def test_claster():
#     rock = Rock(data=[3, 5, 9], eps=4, number_of_clasters=2 )
#     rock.cluster([3, 5, 7], 2)
#     assert True
