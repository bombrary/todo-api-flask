import pytest


def test_get_all(client):
    res = client.get('/todo/')
    assert res.get_json() == []

    contents = ["aaa", "bbb", "ccc"]
    for i, content in enumerate(contents):
        res = client.post('/todo/', json={'content': content})
        assert res.get_json() == i + 1

    res = client.get('/todo/')
    for content, todo in zip(contents, res.get_json()):
        assert content == todo['content']


def test_get(client):
    res = client.get('/todo/1/')
    assert res.status_code == 404

    todo_req = {'id': 1, 'content': '部屋の掃除'}
    client.post('/todo/', json={'content': todo_req['content']})
    res = client.get('/todo/1/')
    todo_res = res.get_json()
    assert todo_req['id'] == todo_res['id']
    assert todo_req['content'] == todo_res['content']


@pytest.mark.parametrize(('json_data'), (
    ({'content': 1}),
    ({'foo': 'bar'}),
))
def test_post_bad(client, json_data):
    res = client.post('/todo/', json=json_data)
    assert res.status_code == 400


def test_post(client):
    res = client.post('/todo/', json={'content': 'foo'})
    assert res.status_code == 200
    assert res.get_json() == 1


def test_delete(client):
    res = client.delete('/todo/1/')
    assert res.status_code == 404

    client.post('/todo/', json={'content': 'foo'})
    res = client.delete('/todo/1/')
    assert res.status_code == 200


@pytest.mark.parametrize(('json_data'), (
    ({'content': 1}),
    ({'foo': 'bar'}),
))
def test_put_bad(client, json_data):
    res = client.put('/todo/1/', json=json_data)
    assert res.status_code == 404

    client.post('/todo/', json={'content': 'foo'})
    res = client.put('/todo/1/', json=json_data)
    assert res.status_code == 400


def test_put(client):
    json_data = {'content': 'foo'}
    res = client.put('/todo/1/', json=json_data)
    assert res.status_code == 404

    client.post('/todo/', json=json_data)
    res = client.put('/todo/1/', json=json_data)
    assert res.status_code == 200


def test_not_json(client):
    res = client.post('/todo/', data='not json data')
    assert res.status_code == 400

    client.post('/todo/', json={'content': 'foo'})
    res = client.put('/todo/1/', data='not json data')
    assert res.status_code == 400
