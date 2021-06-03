import json


def test_get_all(client):
    res = client.get('/todo/')
    assert res.get_json() == []

    contents = ["aaa", "bbb", "ccc"]
    for content in contents:
        res = client.post('/todo/', json={'content': content})

    res = client.get('/todo/')
    for content, todo in zip(contents, res.get_json()):
        assert content == todo['content']
