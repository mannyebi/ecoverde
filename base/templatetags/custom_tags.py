from django import template
from random import randint

register = template.Library()


def cutter(list, args):
    return list[args]


def random(imagelist):
    randomnum = randint(0, len(imagelist)+1)
    return imagelist[randomnum]


register.filter('cutter', cutter)
register.filter('random', random)