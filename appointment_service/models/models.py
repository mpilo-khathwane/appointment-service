import os
import json
import datetime

from mongoengine import *
from mongoengine import signals

from mongoengine.errors import NotUniqueError
from appointment_service.configuration import Config


def handler(event):
    """Signal decorator to allow use of callback functions as class decorators."""
    def decorator(fn):
        def apply(cls):
            event.connect(fn, sender=cls)
            return cls

        fn.apply = apply
        return fn
    return decorator


@handler(signals.pre_save)
def update_modified(sender, document):
    document.modified = datetime.datetime.now()


@update_modified.apply
class Appointment(Document):

    def __repr__(self):
        return "{}".format(
            self.__class__.__name__,
        )
