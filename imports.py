import torch
import matplotlib.pyplot as plt

if torch.cuda.is_available():
    DEVICE = torch.device("cuda")
elif torch.backends.mps.is_available():
    DEVICE = torch.device("mps")
else:
    DEVICE = torch.device("cpu")
DEVICE = torch.device("cpu")

class np:
    nan = torch.nan
    float32 = torch.float32
    inf = torch.tensor(float("inf"), device=DEVICE)

    @staticmethod
    def array(*args, **kwargs):
        return torch.tensor(*args, **kwargs, requires_grad=False, device=DEVICE)

    @staticmethod
    def asarray(*args, **kwargs):
        return torch.tensor(*args, **kwargs, requires_grad=False, device=DEVICE)

    class linalg:
        @staticmethod
        def norm(*args, **kwargs):
            return torch.linalg.norm(*args, **kwargs)

    @staticmethod
    def cross(*args, **kwargs):
        return torch.cross(*args, **kwargs)

    @staticmethod
    def vstack(*args, **kwargs):
        return torch.vstack(*args, **kwargs)

    @staticmethod
    def clip(*args, **kwargs):
        return torch.clip(*args, **kwargs)

    @staticmethod
    def dot(*args, **kwargs):
        return torch.dot(*args, **kwargs)

    @staticmethod
    def linspace(*args, **kwargs):
        return torch.linspace(*args, **kwargs, requires_grad=False, device=DEVICE)

    @staticmethod
    def ones(*args, **kwargs):
        return torch.ones(*args, **kwargs, requires_grad=False, device=DEVICE)

    @staticmethod
    def dstack(*args, **kwargs):
        return torch.dstack(*args, **kwargs)

    @staticmethod
    def meshgrid(*args, **kwargs):
        return torch.meshgrid(*args, **kwargs)

    @staticmethod
    def swapaxes(*args, **kwargs):
        return torch.swapaxes(*args, **kwargs)

    @staticmethod
    def reshape(*args, **kwargs):
        return torch.reshape(*args, **kwargs)

    @staticmethod
    def tile(*args, **kwargs):
        return torch.tile(*args, **kwargs)

    @staticmethod
    def matmul(*args, **kwargs):
        return torch.matmul(*args, **kwargs)

    @staticmethod
    def full_like(*args, **kwargs):
        return torch.full_like(*args, **kwargs, requires_grad=False, device=DEVICE)

    @staticmethod
    def sum(*args, **kwargs):
        return torch.sum(*args, **kwargs)

    @staticmethod
    def broadcast_to(*args, **kwargs):
        return torch.broadcast_to(*args, **kwargs)

    @staticmethod
    def sqrt(*args, **kwargs):
        return torch.sqrt(*args, **kwargs)

    @staticmethod
    def stack(*args, **kwargs):
        return torch.stack(*args, **kwargs)

    @staticmethod
    def argmin(*args, **kwargs):
        return torch.argmin(*args, **kwargs)

    @staticmethod
    def isnan(*args, **kwargs):
        return torch.isnan(*args, **kwargs)

    @staticmethod
    def min(*args, **kwargs):
        return torch.min(*args, **kwargs).values

    @staticmethod
    def full(*args, **kwargs):
        return torch.full(*args, **kwargs, requires_grad=False, device=DEVICE)

    @staticmethod
    def empty_like(*args, **kwargs):
        return torch.empty_like(*args, **kwargs, requires_grad=False, device=DEVICE)

