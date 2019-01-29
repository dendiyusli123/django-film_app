# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Film(models.Model):
    t_rating = 0
    rating_u = 1
    rating_o = 2
    rating_b = 3
    ratings = (
        (t_rating, 'tr - tanpa rating'),
        (rating_u, 'ru - umum'),
        (rating_o, 'ro - pengawasan ortu'),
        (rating_b, 'rb - dibatasi')
    )

    judul = models.CharField(max_length=140)
    plot = models.TextField()
    tahun = models.PositiveIntegerField()
    rating = models.IntegerField(
        choices = ratings,
        default = t_rating
    )
    runtime = models.PositiveIntegerField()
    website = models.URLField(
        blank = True
    )

    direktur = models.ForeignKey(
        to = 'Orang',
        on_delete = models.SET_NULL,
        related_name = 'diarahkan',
        null = True,
        blank = True
    )

    pengarangs = models.ManyToManyField(
        to = 'Orang',
        related_name = 'menulis_kredit',
        blank = True
    )

    aktors = models.ManyToManyField(
        to = 'Orang',
        through = 'Role',
        blank = True
    )

    class Meta:
        ordering = ('-tahun', 'judul')

    def __str__(self):
        return '{} ({})'.format(self.judul, self.tahun)

class Orang(models.Model):
    nama_awal = models.CharField(max_length=140)
    nama_akhir = models.CharField(max_length=140)
    lahir = models.DateField()
    mati = models.DateField(null=True, blank=True)

    class Meta:
        ordering = (
            'nama_akhir', 'nama_awal'
        )

    def __str__(self):
        if self.mati:
            return '{}, {} ({}-{})'.format(
                self.nama_awal,
                self.nama_akhir,
                self.lahir,
                self.mati
            )
        return '{}, {} ({})'.format(
            self.nama_awal,
            self.nama_akhir,
            self.lahir
        )

class Role(models.Model):
    film = models.ForeignKey(Film, on_delete = models.DO_NOTHING)
    orang = models.ForeignKey(Orang, on_delete=models.DO_NOTHING)
    nama = models.CharField(max_length=140)

    def __str__(self):
        return "{} {} {}".format(self.movie_id, self.orang_id, self.nama)

    class Meta:
        unique_together = (
            'film',
            'orang',
            'nama'
        )
    