# OptionPricingMonteCarloSim
Vanilla/European and Asian option pricing using Monte Carlo simulation

### Monte Carlo Option Pricing

- We can thus simulate the security price under the risk-neutral measure (i.e., with drift $r$) and compute the expected intrinsic value of the option at time, and discount it back to time 0 by multiplying it with $e^{-rT}.

- We repeat this many times, we compute the average over all the resulting sample prices, which yields an approximation to the theoretically fair option price.

### Parameters for Risk-Neutral Option Pricing

- $S_0$ - Initial price of underlying security
- $\sigma$ - Volatility of underlying security 
- $T$ - Time to maturity (annualised)
- $r$ - Risk-free interest rate


### Monte Carlo European Valuation 

- For a European option, the intrinsic value is not path-dependent

- Under risk-neutral probabilities, we use geometric Brownian motion (GBM)

$S_T  = S_0 \cdot exp( (r - \frac{\sigma^2}{2})T + \sigma \sqrt{T}z      )$
