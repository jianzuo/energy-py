from energypy.agent import random_policy
from energypy.agent.memory import Buffer
from energypy.datasets import *
from energypy.envs.battery import Battery
from energypy.envs.gym_wrappers import GymWrapper


registry = {
    'lunar': GymWrapper,
    'pendulum': GymWrapper,
    'battery': Battery,
    'random-dataset': RandomDataset,
    'random-policy': random_policy.make,
    'nem-dataset': NEMDataset,
    'buffer': Buffer,
}


def make(name=None, *args, **kwargs):
    if name is None:
        name = kwargs['name']
    return registry[name](*args, **kwargs)
