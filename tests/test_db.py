def test_init_db(runner, monkeypatch):
    class Recorder:
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('todo_list.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
