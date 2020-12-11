# @Author: ASHISH SASMAL <ashish>
# @Date:   12-12-2020
# @Last modified by:   ashish
# @Last modified time: 12-12-2020

from django import template
from users.models import *
from django.db.models import Q

register = template.Library()

@register.simple_tag
def frndscount(user):
    i1 = Friends.objects.filter(Q(user1=user)|Q(user2=user)).count()
    return i1
