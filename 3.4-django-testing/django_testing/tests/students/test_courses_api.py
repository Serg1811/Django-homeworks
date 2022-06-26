import random
import string
import pytest

from pprint import pprint
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course

path = "/api/v1/"


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):

    count = Course.objects.count()
    courses = course_factory(_quantity=1)
    course_id = courses[0].id
    course_name = courses[0].name

    response = client.get(f'{path}courses/{course_id}/')
    data = response.json()
    assert response.status_code == 200
    assert Course.objects.count() == count + len(courses)
    assert course_id == data['id'] and course_name == data['name']


@pytest.mark.django_db
def test_get_list_courses(client, course_factory):

    count = Course.objects.count()
    courses = course_factory(_quantity=10)
    courses_added = set()
    for course in courses:
        course_id = course.id
        course_name = course.name
        courses_added |= {('id', course_id), ('name', course_name)}
    response = client.get(f'{path}courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == count + len(courses)
    courses_response = {(key, value) for course_response in data for key, value in course_response.items()
                        if key != 'students'}
    assert courses_added <= courses_response


@pytest.mark.django_db
def test_get_courses_filter_id(client, course_factory):

    courses = course_factory(_quantity=10)
    course_id = courses[0].id
    course_name = courses[0].name
    response = client.get(f'{path}courses/?id={course_id}')
    assert response.status_code == 200
    data = response.json()
    for course in data:
        if course['id'] == course_id:
            assert course['name'] == course_name
            break


@pytest.mark.django_db
def test_get_courses_filter_id(client, course_factory):

    courses = course_factory(_quantity=10)
    courses_name = {}
    for course in courses:
        course_id = course.id
        course_name = course.name
        courses_name.setdefault(course_name, set())
        courses_name[course_name] |= {course_id}
    for name, id_set in courses_name.items():
        response = client.get(f'{path}courses/?name={name}')
        assert response.status_code == 200
        data = response.json()
        assert len(data) == len(id_set)
        course_name_id = {course['id'] for course in data}
        assert id_set <= course_name_id


@pytest.mark.django_db
def test_create_course(client, course_factory):

    name = generate_random_string(5)
    response = client.post(f'{path}courses/', data={'name': name})
    assert response.status_code == 201
    course = response.json()
    course_db = Course.objects.get(id=course['id'])
    assert course['name'] == course_db.name


@pytest.mark.django_db
def test_change_course(client, course_factory):
    course_factory(_quantity=10)
    courses = Course.objects.all()
    course = random.choice(courses)
    while True:
        name = generate_random_string(5)
        if name != course.name:
            break
    response = client.patch(f'{path}courses/{course.id}/', data={'name': name})
    assert response.status_code == 200
    course_db = Course.objects.get(id=course.id)
    assert name == course_db.name


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course_factory(_quantity=10)
    courses = Course.objects.all()
    course = random.choice(courses)
    response = client.delete(f'{path}courses/{course.id}/')
    assert response.status_code == 204
    course_db = Course.objects.filter(id=course.id)
    assert len(course_db) == 0
