import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 845786312 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    count = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    value = proportions_ztest(count, nobs)[1]
    return value < 0.02 # Ваш ответ, True или False
