from .base_mopo import mopo_params, deepcopy
from ray import tune

params = deepcopy(mopo_params)
params.update({
    'type': 'COMBO',
    'domain': 'hopper',
    'task': 'medium-expert-v0',
    'exp_name': 'hopper_medium_expert_COMBO'
})
params['kwargs'].update({
    'type': 'COMBO',
    'pool_load_path': 'd4rl/hopper-medium-expert-v0',
    'pool_load_max_size': 10**6,
    'rollout_length': 5,
    'penalty_coeff': 0.0,
    'deterministic': False,
    'beta': tune.grid_search([0.1, 0.5, 1.0, 2.0])
})