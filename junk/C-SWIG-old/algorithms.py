# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_algorithms', [dirname(__file__)])
        except ImportError:
            import _algorithms
            return _algorithms
        if fp is not None:
            try:
                _mod = imp.load_module('_algorithms', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _algorithms = swig_import_helper()
    del swig_import_helper
else:
    import _algorithms
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class Individual_ld(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Individual_ld, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Individual_ld, name)
    __repr__ = _swig_repr
    __swig_setmethods__["fitness"] = _algorithms.Individual_ld_fitness_set
    __swig_getmethods__["fitness"] = _algorithms.Individual_ld_fitness_get
    if _newclass:fitness = _swig_property(_algorithms.Individual_ld_fitness_get, _algorithms.Individual_ld_fitness_set)
    __swig_setmethods__["genotype"] = _algorithms.Individual_ld_genotype_set
    __swig_getmethods__["genotype"] = _algorithms.Individual_ld_genotype_get
    if _newclass:genotype = _swig_property(_algorithms.Individual_ld_genotype_get, _algorithms.Individual_ld_genotype_set)
    __swig_setmethods__["chromlen"] = _algorithms.Individual_ld_chromlen_set
    __swig_getmethods__["chromlen"] = _algorithms.Individual_ld_chromlen_get
    if _newclass:chromlen = _swig_property(_algorithms.Individual_ld_chromlen_get, _algorithms.Individual_ld_chromlen_set)
    def __init__(self, *args): 
        this = _algorithms.new_Individual_ld(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _algorithms.delete_Individual_ld
    __del__ = lambda self : None;
Individual_ld_swigregister = _algorithms.Individual_ld_swigregister
Individual_ld_swigregister(Individual_ld)

class EA_ld(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, EA_ld, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EA_ld, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_getmethods__["popsize"] = _algorithms.EA_ld_popsize_get
    if _newclass:popsize = _swig_property(_algorithms.EA_ld_popsize_get)
    __swig_getmethods__["chromlen"] = _algorithms.EA_ld_chromlen_get
    if _newclass:chromlen = _swig_property(_algorithms.EA_ld_chromlen_get)
    __swig_setmethods__["evaluator"] = _algorithms.EA_ld_evaluator_set
    __swig_getmethods__["evaluator"] = _algorithms.EA_ld_evaluator_get
    if _newclass:evaluator = _swig_property(_algorithms.EA_ld_evaluator_get, _algorithms.EA_ld_evaluator_set)
    __swig_setmethods__["evaluation_counter"] = _algorithms.EA_ld_evaluation_counter_set
    __swig_getmethods__["evaluation_counter"] = _algorithms.EA_ld_evaluation_counter_get
    if _newclass:evaluation_counter = _swig_property(_algorithms.EA_ld_evaluation_counter_get, _algorithms.EA_ld_evaluation_counter_set)
    __swig_setmethods__["tmax"] = _algorithms.EA_ld_tmax_set
    __swig_getmethods__["tmax"] = _algorithms.EA_ld_tmax_get
    if _newclass:tmax = _swig_property(_algorithms.EA_ld_tmax_get, _algorithms.EA_ld_tmax_set)
    __swig_setmethods__["best"] = _algorithms.EA_ld_best_set
    __swig_getmethods__["best"] = _algorithms.EA_ld_best_get
    if _newclass:best = _swig_property(_algorithms.EA_ld_best_get, _algorithms.EA_ld_best_set)
    __swig_setmethods__["t"] = _algorithms.EA_ld_t_set
    __swig_getmethods__["t"] = _algorithms.EA_ld_t_get
    if _newclass:t = _swig_property(_algorithms.EA_ld_t_get, _algorithms.EA_ld_t_set)
    def run(self): return _algorithms.EA_ld_run(self)
    def initialize(self): return _algorithms.EA_ld_initialize(self)
    def generation(self): return _algorithms.EA_ld_generation(self)
    def operators(self): return _algorithms.EA_ld_operators(self)
    def termination(self): return _algorithms.EA_ld_termination(self)
    def P(self): return _algorithms.EA_ld_P(self)
    __swig_destroy__ = _algorithms.delete_EA_ld
    __del__ = lambda self : None;
EA_ld_swigregister = _algorithms.EA_ld_swigregister
EA_ld_swigregister(EA_ld)

class rQIEA_ld(EA_ld):
    __swig_setmethods__ = {}
    for _s in [EA_ld]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, rQIEA_ld, name, value)
    __swig_getmethods__ = {}
    for _s in [EA_ld]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, rQIEA_ld, name)
    __repr__ = _swig_repr
    def clone(self): return _algorithms.rQIEA_ld_clone(self)
    __swig_setmethods__["Pc"] = _algorithms.rQIEA_ld_Pc_set
    __swig_getmethods__["Pc"] = _algorithms.rQIEA_ld_Pc_get
    if _newclass:Pc = _swig_property(_algorithms.rQIEA_ld_Pc_get, _algorithms.rQIEA_ld_Pc_set)
    def __init__(self, *args): 
        this = _algorithms.new_rQIEA_ld(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _algorithms.delete_rQIEA_ld
    __del__ = lambda self : None;
    def initialize(self): return _algorithms.rQIEA_ld_initialize(self)
    def operators(self): return _algorithms.rQIEA_ld_operators(self)
    def getGeneration(self, *args): return _algorithms.rQIEA_ld_getGeneration(self, *args)
    def Q(self): return _algorithms.rQIEA_ld_Q(self)
    def getQ(self, *args): return _algorithms.rQIEA_ld_getQ(self, *args)
    def bounds(self, *args): return _algorithms.rQIEA_ld_bounds(self, *args)
rQIEA_ld_swigregister = _algorithms.rQIEA_ld_swigregister
rQIEA_ld_swigregister(rQIEA_ld)


