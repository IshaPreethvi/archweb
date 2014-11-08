from django_jinja import library
from markupsafe import Markup


@library.global_function
def country_flag(country):
    if not country:
        return ''
    html = '<span class="fam-flag fam-flag-%s" title="%s"></span> ' % (
            unicode(country.code).lower(), unicode(country.name))
    return Markup(html)


@library.filter
def duration(value):
    if not value and type(value) != timedelta:
        return u''
    # does not take microseconds into account
    total_secs = value.seconds + value.days * 24 * 3600
    mins = total_secs // 60
    hrs, mins = divmod(mins, 60)
    return '%d:%02d' % (hrs, mins)


@library.filter
def floatvalue(value, arg=2):
    if value is None:
        return u''
    return '%.*f' % (arg, value)

# vim: set ts=4 sw=4 et:
