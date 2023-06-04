from .base_mopo import mopo_params, deepcopy
from ray import tune

params = deepcopy(mopo_params)
params.update({
    'type': 'COMBO',
    'domain': 'halfcheetah',
    'task': 'medium-expert-v0',
    'exp_name': 'halfcheetah_medium_expert_COMBO',

})
params['kwargs'].update({
    'pool_load_path': 'd4rl/halfcheetah-medium-expert-v0',
    'pool_load_max_size': 2 * 10**6,
    'rollout_length': 5,
    'penalty_coeff': 0.0,
    'deterministic': False,
    'real_ratio': tune.grid_search([0.05]), #, 0.2]),
    'num_networks': 7,
    'num_elites': 5,
    'beta': tune.grid_search([0.1]), #, 1.0])
})