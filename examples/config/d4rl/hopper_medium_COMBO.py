from .base_mopo import mopo_params, deepcopy
from ray import tune

params = deepcopy(mopo_params)
params.update({
    'type': 'COMBO',
    'domain': 'hopper',
    'task': 'medium-v0',
    'exp_name': 'hopper_medium_COMBO'
})
params['kwargs'].update({
    'type': 'COMBO',
    'pool_load_path': 'd4rl/hopper-medium-v0',
    'pool_load_max_size': 10**6,
    'rollout_length': 5,
    'penalty_coeff': 0.0,
    'deterministic': False,
    'beta': tune.grid_search([0.1, 1.0]),
    'real_ratio': tune.grid_search([0.5, 0.9]),
})