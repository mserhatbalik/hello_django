from django.urls import path

# Import views.py from current directory.
# Use .. to refer to parent directory. Use ... to refer to grandparent directory.
# Using without dot notation refers to sys.path packages, which is not what we want in this situation.
from .views import home_page_view

urlpatterns = [
    path("", home_page_view)
]