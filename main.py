import numpy as np
from typing import Callable, List, Dict, Union, Any


class OptionPricingMcs:

    def __init__(self, S0: Union[int,float], K: int, T, r, sigma, I, opt_type: str):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.I = I
        self.opt_type = opt_type

    def european_option_mcs(self):
        # Simulate GBM to compute security value at maturity T
        S = self.S0 * np.exp((self.r - 0.5 * (self.sigma**2) * self.T) 
                         + (self.sigma * np.sqrt(self.T) * np.random.normal(size = self.I)))
        # Compute intrinsic value of option 
        C = np.maximum(S-self.K,0) if self.opt_type == "call" else np.max(self.K-S,0)
        # Compute mean intrinsic value of option
        C_mean = np.mean(C)
        # Present value using continuos compounding
        C_pv = self.pv_continuos(C_mean)

        return C_pv
        
    def asian_option_mcs(self, M):
        # Step in simulating GBM
        dt = self.T/M
        # Simulate I paths with M time steps
        S = S0 * np.exp(np.cumsum((r - 0.5 * sigma**2 ) * dt + sigma * np.sqrt( dt ) 
                        * np.random.standard_normal(( M , I )), axis = 0 )) 
        # Compute intrinsic value of option 
        C = np.maximum((np.mean(S,axis=0)-self.K),0) 
        # Compute mean intrinsic value of option
        C_mean = np.mean(C)
        # Present value using continuos compounding
        C_pv = self.pv_continuos(C_mean)

        return C_pv


    def pv_continuos(self, C_mean):
        C_pv = np.exp(-self.r * self.T) * C_mean
        return C_pv
        
    
if __name__ == "__main__":

    S0 =100.;K=105.;T=1.0;M=200 
    r=0.02;sigma=0.1;I=100000
    opt_type = "call"

    opt = OptionPricingMcs(S0, K, T, r, sigma, I, opt_type)

    eur_opt = opt.european_option_mcs()
    asi_opt = opt.asian_option_mcs(M)

    print(eur_opt)
    print(asi_opt)