from django.test import SimpleTestCase

from ..utils import render, setup


class TruncatecharsTests(SimpleTestCase):

    @setup({'truncatechars01': '{{ a|truncatechars:5 }}'})
    def test_truncatechars01(self):
        output = render('truncatechars01', {'a': 'Testing, testing'})
        self.assertEqual(output, 'Te...')

    @setup({'truncatechars02': '{{ a|truncatechars:7 }}'})
    def test_truncatechars02(self):
        output = render('truncatechars02', {'a': 'Testing'})
        self.assertEqual(output, 'Testing')
