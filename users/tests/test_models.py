import pytest

from ..models import User

pytestmark = pytest.mark.django_db

def test_create_user():
	user = User.objects.create_user(username="testuser", email="test@email.com", password="testing321")

	assert user.username == "testuser"
	assert user.email == "test@email.com"
	assert user.is_active
	assert not user.is_staff
	assert not user.is_superuser


def test_create_superuser():
	user = User.objects.create_superuser(username="admin_test", email="admin@email.com", password="testing321")

	assert user.username == "admin_test"
	assert user.email == "admin@email.com"
	assert user.is_active
	assert user.is_staff
	assert user.is_superuser

