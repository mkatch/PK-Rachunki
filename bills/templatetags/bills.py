from django import template

register = template.Library()

@register.inclusion_tag('bills/entry_form.html')
def show_entry_form(form):
    return {'form': form}