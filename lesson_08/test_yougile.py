import pytest
import requests

from YouGileApi import YouGileApi


api = YouGileApi("https://yougile.com")

# ПОЗИТИВНЫЕ ТЕСТЫ

def test_list_project():
    body = api.list_project()
    assert len(body) > 0

def test_create_project():
    # получить количество проектов
    body = api.list_project()
    len_before = body['content']
    # создать новый проект
    title = "Autotest"
    result = api.create_project(title)
    # получить id нового проекта
    id_project = result["id"] 
    # поучить новое количество проектов
    body = api.list_project()
    len_after = body['content']
    # сравнить количество проектов до и после соданного
    assert len_after > len_before
    # сравнить id созданного проекта
    assert len_after[-1]["id"] == id_project

def test_edit_project():
    # получить количество проектов
    body = api.list_project()
    len_before = body['content']

    # создать новый проект
    title = "три"
    result = api.create_project(title)
    # получить id нового проекта
    new_id_progect = result["id"] 

    # изменить название проекта
    new_title = "put"
    edited = api.edit_progect(new_id_progect, new_title)

    # поучить новое количество проектов
    body = api.list_project()
    len_after = body['content']

    # сравнить количество проектов до и после соданного
    assert len_after > len_before
    # сравнить id созданного проекта
    assert len_after[-1]["id"] == new_id_progect
    # сравнить название созданного проекта
    assert len_after[-1]["title"] == "put"

def test_search_by_id_progect():
    # получить количество проектов
    body = api.list_project()
    len_before = body['content']

    # создать новый проект
    title = "поиск по id"
    result = api.create_project(title)
    # получить id нового проекта
    new_id_progect = result["id"] 

    # найти проекта по ID
    body = api.search_by_id_progect(new_id_progect)
    timestamp = body['timestamp']

    # поучить новое количество проектов
    body = api.list_project()
    len_after = body['content']

    # сравнить количество проектов до и после соданного
    assert len_after > len_before

    # сравнить id созданного проекта
    assert len_after[-1]["id"] == new_id_progect

    # сравнить значение параметра timestamp
    assert len_after[-1]["timestamp"] == timestamp

# НЕГАТИВНЫЕ ТЕСТЫ

# Оставить обязательное поле пустым

def test_create_project_negativ():
    # получить количество проектов
    body = api.list_project()
    len_before = body['content']
    # создать новый проект
    title = ""
    result = api.create_project(title)
    # получить id нового проекта
    id_project = result["id"] 
    # поучить новое количество проектов
    body = api.list_project()
    len_after = body['content']
    # сравнить количество проектов до и после соданного
    assert len_after > len_before
    # сравнить id созданного проекта
    assert len_after[-1]["id"] == id_project

# Запросить список проектов с неправильным URL

def test_list_project_negativ():
    body = api.list_project_negativ()
    assert len(body) > 0

# Проверка нового названия проекта

def test_edit_project_negativ():
    # получить количество проектов
    body = api.list_project()
    len_before = body['content']

    # создать новый проект
    title = "put"
    result = api.create_project(title)
    # получить id нового проекта
    new_id_progect = result["id"] 

    # изменить название проекта
    new_title = "три"
    edited = api.edit_progect(new_id_progect, new_title)

    # поучить новое количество проектов
    body = api.list_project()
    len_after = body['content']

    # сравнить количество проектов до и после соданного
    assert len_after > len_before
    # сравнить id созданного проекта
    assert len_after[-1]["id"] == new_id_progect
    # сравнить название созданного проекта
    assert len_after[-1]["title"] == "put"
