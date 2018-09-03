import datetime

from django import template
from django.utils import timezone
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter
def add_label_class(field, class_name):
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })


@register.filter(name='addplaceholder')
def addplaceholder(value, arg):
    return value.as_widget(attrs={'placeholder': arg})


@register.filter
def dateoffset(value, offset):
    """
    Shift a date by given offset.
    Example: dateoffset("2018-10-21", 2) => "2018-10-23"
    """
    newdate = datetime.datetime.strptime(value, '%Y-%m-%d') + timezone.timedelta(offset)
    return newdate.strftime('%Y-%m-%d')


@register.filter
def yyyymmdd_to_ddmmyyyy(value):
    if isinstance(value, datetime.date):
        newdate = value
    else:
        newdate = datetime.datetime.strptime(value, '%Y-%m-%d')
    return newdate.strftime('%d-%m-%Y')


@register.filter
def yyyymmdd(value):
    return value.strftime('%Y-%m-%d')


@register.filter
def join_good_runs(list_of_run_numbers):
    """
    takes a list of run numbers and wraps them in <span class="good-runs">
    """
    if list_of_run_numbers:
        rendered_string = '<span class="good-runs">'
        rendered_string += ", ".join(str(x) for x in list_of_run_numbers)
        rendered_string += '</span>'
        return mark_safe(rendered_string)
    return ""


@register.filter
def join_bad_runs(list_of_run_numbers):
    """
    takes a list of run numbers and wraps them in <span class="bad-runs">
    """
    if list_of_run_numbers:
        rendered_string = '<span class="bad-runs">'
        rendered_string += ", ".join(str(x) for x in list_of_run_numbers)
        rendered_string += '</span>'
        return mark_safe(rendered_string)
    return ""


@register.filter
def as_date(yyyy_mm_dd):
    """
    :param yyyy_mm_dd: date string
    :return: date object
    """

    try:
        return datetime.datetime.strptime(yyyy_mm_dd, '%Y-%m-%d').date()
    except ValueError as e:
        if yyyy_mm_dd == "":
            return ""
        return e


@register.filter
def user(value, arg):
    """
    filetrs the runinfo
    """
    return value.filter(userid=arg)
