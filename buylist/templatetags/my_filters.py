from django import template

register = template.Library()


@register.filter(name='add_class')
def add_class(value, arg):
    # print(f'Input: {value} \n Arg: {arg}')
    return value.as_widget(attrs={'class': arg})

# recebe um input(values, a tag) e a classe(arg);
# depois adiciona nesse input a classe
# form_product.description é o input nesse caso
