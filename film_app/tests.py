# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test.client import RequestFactory
from django.urls.base import reverse

from film_app.models import Film
from film_app.views import FilmList

class FilmListPaginationTestCase(TestCase):
    ACTIVE_PAGINATION_HTML = """
    <li class="page-item active">
        <a href="{}?page={}" class="page-link">{}</a>
    </li>
    """

    def setUp(self):
        for n in range(15):
            Film.objects.create(
                judul = 'Judul {}'.format(n),
                tahun = 2015 + n,
                runtime = 105,
            )

    def testUtamaPage(self):
        film_list_path = reverse('film_app:FilmList')
        request = RequestFactory().get(path=film_list_path)
        response = FilmList.as_view() (request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(
                film_list_path, 1, 1),
            response.rendered_content
        )
