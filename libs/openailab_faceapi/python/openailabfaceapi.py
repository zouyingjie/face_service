# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')
def swig_import_helper():
    import importlib
    pkg = __name__.rpartition('.')[0]
    mname = '.'.join((pkg, '_openailabfaceapi')).lstrip('.')
    try:
        return importlib.import_module(mname)
    except ImportError:
        return importlib.import_module('_openailabfaceapi')
_openailabfaceapi = swig_import_helper()
del swig_import_helper
del _swig_python_version_info

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def initial(log_path, model_path):
    return _openailabfaceapi.initial(log_path, model_path)
initial = _openailabfaceapi.initial

def deinitial():
    return _openailabfaceapi.deinitial()
deinitial = _openailabfaceapi.deinitial
class FaceRect(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FaceRect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FaceRect, name)
    __repr__ = _swig_repr
    __swig_setmethods__["left"] = _openailabfaceapi.FaceRect_left_set
    __swig_getmethods__["left"] = _openailabfaceapi.FaceRect_left_get
    if _newclass:
        left = property(_openailabfaceapi.FaceRect_left_get, _openailabfaceapi.FaceRect_left_set)
    __swig_setmethods__["top"] = _openailabfaceapi.FaceRect_top_set
    __swig_getmethods__["top"] = _openailabfaceapi.FaceRect_top_get
    if _newclass:
        top = property(_openailabfaceapi.FaceRect_top_get, _openailabfaceapi.FaceRect_top_set)
    __swig_setmethods__["width"] = _openailabfaceapi.FaceRect_width_set
    __swig_getmethods__["width"] = _openailabfaceapi.FaceRect_width_get
    if _newclass:
        width = property(_openailabfaceapi.FaceRect_width_get, _openailabfaceapi.FaceRect_width_set)
    __swig_setmethods__["height"] = _openailabfaceapi.FaceRect_height_set
    __swig_getmethods__["height"] = _openailabfaceapi.FaceRect_height_get
    if _newclass:
        height = property(_openailabfaceapi.FaceRect_height_get, _openailabfaceapi.FaceRect_height_set)

    def __init__(self):
        this = _openailabfaceapi.new_FaceRect()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _openailabfaceapi.delete_FaceRect
    def __del__(self):
        return None
# Register FaceRect in _openailabfaceapi:
_openailabfaceapi.FaceRect_swigregister(FaceRect)


def FaceExisted(jpegFileName):
    return _openailabfaceapi.FaceExisted(jpegFileName)
FaceExisted = _openailabfaceapi.FaceExisted

def FaceQualityOK(jpegFileName, rectangle, threshold):
    return _openailabfaceapi.FaceQualityOK(jpegFileName, rectangle, threshold)
FaceQualityOK = _openailabfaceapi.FaceQualityOK

def FaceIsSamePerson(jpegFileNameList, threshold):
    return _openailabfaceapi.FaceIsSamePerson(jpegFileNameList, threshold)
FaceIsSamePerson = _openailabfaceapi.FaceIsSamePerson

def BestFacePicture(jpegFileNameList, threshold):
    return _openailabfaceapi.BestFacePicture(jpegFileNameList, threshold)
BestFacePicture = _openailabfaceapi.BestFacePicture
# This file is compatible with both classic and new-style classes.


