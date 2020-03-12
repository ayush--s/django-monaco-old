from __future__ import absolute_import, unicode_literals
from django import forms


class MonacoEditorWidget(forms.Textarea):

    def render(self, name, value, attrs=None):
        monaco_attrs = {
            'monaco-editor': 'true',
            'data-language': 'json',
            'data-wordwrap': 'on',
            'data-minimap': 'false'
        }
        monaco_attrs.update(attrs)
        output = super(MonacoEditorWidget, self).render(name, value, monaco_attrs)
        return output

    class Media:
        css = {
            'all': ("monaco.custom.css",)
        }
        js = ('monaco/loader.js', 'monaco.config.js')
