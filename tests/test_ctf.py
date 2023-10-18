import pytest
import numpy as np
from gym_multigrid.envs.ctf import Ctf1v1Env


def test_ctf() -> None:
    map_path: str = "tests/assets/board.txt"

    env = Ctf1v1Env(map_path=map_path)
    obs, _ = env.reset()

    while True:
        action = np.random.choice(list(env.actions_set))
        obs, reward, terminated, truncated, info = env.step(action)
        env.render()
        if terminated or truncated:
            break
