# -*- coding: utf-8 -*-

from odoo import api, models, fields, _


class BlogPost(models.Model):
    _inherit = "blog.post"

    iframe_stream = fields.Text('iFrame Completo src', help="Solo el src del iframe")
    iframe_stream_height = fields.Integer('Altura (px)', default=200)
    iframe_stream_mini = fields.Text('iFrame Tarjeta src', help="Solo el src del iframe mini")
    iframe_stream_mini_height = fields.Integer('Altura (px)', default=50)
    iframe_stream_side = fields.Text('iFrame Lateral src', help="Solo el src del iframe lateral")
    iframe_stream_side_height = fields.Integer('Altura (px)', default=50)
    download_stream = fields.Text('Podcast Download link')


# class Blog(models.Model):
#     _name = 'blog.blog'

