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

\begin{equation}
    S_T  = S_0 \cdot exp( (r - \frac{\sigma^2}{2})T + \sigma \sqrt{T}z      )
\end{equation}

- where $r$ is the risk-free interest rate (instead of the real drift of $S$)

**Non-Path-Dependent Algorithm to Estimate the IntrinsicValue:**

1. Draw random numbers $z_1,z_2,...,z_I$ from the standard normal distribution.
2. For $i \in {1,2,3,...,I}$:

    i). Calculate the underlying security's value at the strike time $T$ by simulating geometric Brownian motion with drift
and volatility $\sigma$ using the above equation.

    ii). Compute the intrinsic value of the option $h_T = max\{ S_T - K, 0 \}$.

    iii). Discount back to the present at the risk-free rate $r$, giving the present value:

\begin{equation*}
    C_i = e^{-rT} h_T
\end{equation*}

3. Output the final estimate by computing the Monte Carlo estimator:

\begin{equation*}
    \hat{C_i} = \frac{\sum^I_{i=1}C_i}{I}
\end{equation*}

### Monte Carlo Asian Options

- The payoff of an Asian option is determined by the average of the price of the underlying over a pre-defined period of time.

- Payoff for a fixed-strike Asian call option:

\begin{equation*}
    C_T = max\{A(0,T)-K,0\}
\end{equation*}

where:

\begin{equation*}
    A(0,T) = \frac{1}{T} \int^T_0 S_t dt
\end{equation*}

If we let $t_i = i \cdot (T/n)$, for $i \in \{0,1,2,...,n\}:

\begin{equation*}
    A(0,T) \approx \frac{1}{n} \sum^{n-1}_{i=0}S_t
\end{equation*}

- The payoff is path dependent, so now we need to simulate intermediate values of $S_t$.

- To simulate GBM at M evenly spaced time intervals $T_i$ with $\Delta = T/M$

\begin{equation*}
    S_{t_k} = S_0 \cdot exp(\sum^k_{i=1}\sigma \sqrt{\Delta}z_i + (\mu - \frac{\sigma^2}{2})\Delta)
\end{equation*}

**Algorithm for Path-Dependant Option Pricing**

1. Draw $I \cdot M$ random numbers from the standard distribution

2. For $i \in \{1,2,...,I \}

    i) Calculate underlying value at times $t_i \in \{ \Delta, 2\Delta, ..., M \Delta = T \}$ by simulating geometric Brownian motion with drift $\mu = r$ and volatility $\sigma$ for $S_{t_k}$.

    ii) Estimate average value of the option $\hat{h_T} = \frac{1}{M} \sum^M_{i=1} S_{t_i}$

    iii) Compute the intrinsic value of the option $h_T = max\{\hat{h_T} - K,0 \}

    iv) Discount back to the present value at the risk-free rate $r$, giving the present value: $C_i = e^{-rT} h_T$

3. Output the final estimate by computing the Monte Carlo estimator:

\begin{equation*}
    \bar{C} = \frac{\sum^I_{i=1}C_i}{I}
\end{equation*}
