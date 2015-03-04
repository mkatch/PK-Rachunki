import django.forms

def _append_to_attr(attrs, key, value):
    attrs[key] = (attrs[key] + ' ' if key in attrs else '') + value


def _with_extra_classes(base, classes):
    class ExtraClassesWidget(base):
        def __init__(self, *args, **kwargs):
            base.__init__(self, *args, **kwargs)
            _append_to_attr(self.attrs, 'class', classes)
    return ExtraClassesWidget

class TextInput(_with_extra_classes(django.forms.TextInput, 'form-control')):
    pass


class TextArea(_with_extra_classes(django.forms.Textarea, 'form-control')):
    pass


class Select(_with_extra_classes(django.forms.Select,
                                 'form-control bs-select')):
    class Media:
        css = {
            'all': ('bootstrap/css/widgets.css',),
        }

class DatePicker(_with_extra_classes(django.forms.TextInput,
                                     'form-control bs-datepicker')):
    class Media:
        css = {
            'all': ('bootstrap-datepicker/css/datepicker3.css',),
        }
        js = (
            'bootstrap-datepicker/js/bootstrap-datepicker.js',
            'bootstrap-datepicker/js/locales/bootstrap-datepicker.pl.js',
            'bootstrap/js/widgets.js',
        )