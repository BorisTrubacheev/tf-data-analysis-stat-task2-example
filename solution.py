import pandas as pd
import numpy as np
from scipy.stats import expon

from scipy.stats import norm


chat_id = 1736726957 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    alpha = 1 - p
    return 2/(17**2)*(expon.ppf(alpha / 2) + x.mean() - 1.5), \
           2/(17**2)*(expon.ppf(1 - alpha / 2) + x.mean() - 4)
