import json


def test_get_all(client):
    mimetype = 'application/json'
    res = client.get('/todo/', mimetype=mimetype)
    assert res.get_json() == []

    contents = ["aaa", "bbb", "ccc"]
    for content in contents:
        data = json.dumps({'content': content})
        res = client.post('/todo/', mimetype=mimetype, data=data)

    res = client.get('/todo/', mimetype=mimetype)
    for content, todo in zip(contents, res.get_json()):
        assert content == todo['content']

