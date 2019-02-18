from django.test import TestCase

# Create your tests here.

namespace=False
app_name=0
abc="4566"
namespace = namespace or app_name or abc
print(namespace)