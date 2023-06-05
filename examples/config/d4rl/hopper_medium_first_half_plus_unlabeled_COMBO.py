from .base_mopo import mopo_params, deepcopy
from ray import tune

params = deepcopy(mopo_params)
params.update({
    'type': 'COMBO',
    'domain': 'hopper',
    'task': 'medium-first-half-plus-unlabeled-v0',
    'exp_name': 'hopper_medium_first_half_plus_unlabeled_COMBO'
})
params['kwargs'].update({
    'type': 'COMBO',
    'pool_load_path': '/home/ikasou/.d4rl/datasets/hopper_medium_first_half_plus_unlabeled_to_min.hdf5',
    'pool_load_max_size': 10**6,
    'rollout_length': 5,
    'penalty_coeff': 0.0,
    'deterministic': False,
    'beta': tune.grid_search([0.1]),
    'num_networks': 7,
    'num_elites': 5,
    'real_ratio': tune.grid_search([0.05]),
})