from django import template
from django.template.defaultfilters import stringfilter
import markdown as md
from markdown.extensions.toc import TocExtension

register = template.Library()


@register.filter
@stringfilter
def show_markdown(text):
    return md.markdown(text , extensions=[
        'markdown.extensions.toc',
        'markdown.extensions.extra',
        'markdown.extensions.abbr',
        'markdown.extensions.attr_list',
        'markdown.extensions.def_list',
        'markdown.extensions.fenced_code',
        'markdown.extensions.footnotes',
        'markdown.extensions.md_in_html',
        'markdown.extensions.tables',
        'markdown.extensions.admonition',
        'markdown.extensions.codehilite',
        'markdown.extensions.legacy_attrs',
        'markdown.extensions.legacy_em',
        'markdown.extensions.meta',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
        'markdown.extensions.smarty',
        'markdown.extensions.wikilinks',
        TocExtension(baselevel=3),

    ])