"""
This module contains classes for representing lazy property
"""

__all__ = ['lazy_property']

class lazy_property(property):
    """
    Decorator for lazy property.

    Calling __set__ does not actually change property value.
    The first call of __get__ makes all required actions and returns value
    The other calls returns the evaluated result, unless __set__ will be called again
    """
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        super().__init__(fget, fset, fdel, doc)

        self._prop_name = '__impl_lazy_' + fget.__name__

    def __set__(self, obj, value):
        setattr(obj, self._prop_name, value)

    def __get__(self, obj, type=None):
        if hasattr(obj, self._prop_name):
            prop = getattr(obj, self._prop_name)

            if prop is not None:
                super().__set__(obj, prop)
                setattr(obj, self._prop_name, None)

        return super().__get__(obj, type)