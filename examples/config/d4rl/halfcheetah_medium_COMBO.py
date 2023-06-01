from .base_mopo import mopo_params, deepcopy
from ray import tune

params = deepcopy(mopo_params)
params.update({
    'type': 'COMBO',
    'domain': 'halfcheetah',
    'task': 'medium-v0',
    'exp_name': 'halfcheetah_medium_COMBO',

})
params['kwargs'].update({
#    'type': 'COMBO',
    'pool_load_path': 'd4rl/halfcheetah-medium-v0',
    'pool_load_max_size': 10**6,
    'rollout_length': 1,
    'penalty_coeff': 0.0,
    'deterministic': False,
    'real_ratio': tune.grid_search([0.05, 0.5, 0.9]),
    'beta': tune.grid_search([0.1, 1.0])
})