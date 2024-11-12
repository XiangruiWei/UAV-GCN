from .util import IO
from .util import str2bool
from .util import str2dict
from .util import DictAction
from .util import import_class
from .gpu import visible_gpu
from .gpu import occupy_gpu
from .gpu import ngpu

class DictAction(argparse.Action):
    """
    argparse action to split arguments into key-value pairs.
    """

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict())
        for value in values:
            key, val = value.split('=')
            getattr(namespace, self.dest)[key] = val