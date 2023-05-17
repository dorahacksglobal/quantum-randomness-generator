# Realization of Bell's theorem certified quantum random number generation using cloud quantum computers

This repository is a collection of DoraHack's experiments for certified quantum random number generation using cloud quantum computers. 

[TOC]

<!--## Glossary

This introduction aims at broad audience with different scientific backgrouds. To make it more intelligible, we list the necessary glossary, including terms and abbreviations.

| **Term** | **Definition** |
| -------- | -------- |
| PRNG     | Pseudo Random Number Generator     |
| QRNG | Quantum Random Number Generator |
|DI-QRNG| Device-independent Random Number generator|
|VRF|Verifiable Random Function|-->


## Random number applications

Randomness refers to the quality of being unpredictable or haphazard. It is an essential concept in various fields, ranging from computer science to statistical analysis. In today's world, randomness plays a crucial role in many applications across different scenarios. 

For example, in cryptography, random numbers are used to generate secure keys and passwords that are difficult to crack. In gaming, random numbers are used to create unpredictable outcomes and add an element of chance, making the experience more exciting and engaging for users. In scientific simulations, random numbers are used to model complex systems and generate experimental data that accurately reflects real-world conditions. By using random numbers as inputs, scientists can test hypotheses and gain insights into the behavior of physical phenomena such as weather patterns or biological processes. In statistics, random numbers are used to create representative samples, which are subsets of larger populations that are used to make inferences about the population as a whole. This is important in fields such as public health, where researchers need to understand how certain diseases affect different segments of the population. By gathering data from randomly selected individuals, researchers can obtain a clearer picture of the disease's prevalence and its impact on various demographic groups.

## Classifications of random number generation

Generally, there are two ways to produce the random numbers: PRNG (Pseudo random number generator) and QRNG (quantum random number generator). 

Pseudo random number generators (PRNGs) are algorithms that generate sequences of numbers that appear to be random but are actually deterministic, meaning that the output is entirely dependent on the algorithm and a seed value. Examples of PRNGs include linear congruential generators (LCGs) and Mersenne Twister, which is the default algorithms in MATLAB, Mathematica and Python. In contrast, quantum random number generators (QRNGs) use quantum mechanical processes to generate truly random numbers. Examples of QRNGs include devices that measure vacuum fluctuations or phase fluctuations of amplified spoteneous emission. Recently, utilizing integrated balanced homodyne detector, the QRNG of 100Gbit/s is demonstrated [1].

While both PRNGs and QRNGs can be used for applications that require randomness, QRNGs have several advantages over PRNGs. First and foremost, QRNGs produce truly unpredictable numbers that cannot be reproduced, whereas PRNGs produce numbers that could potentially be predicted or hacked. This makes QRNGs particularly useful in fields such as cryptography and security, where high-quality randomness is essential to prevent attacks. Additionally, QRNGs are not subject to the same biases or weaknesses that can arise in PRNGs due to flaws in their algorithms or implementation. Finally, as quantum computing continues to advance, QRNGs are likely to become even more powerful and versatile tools for generating randomness.

## DI-QRNG and Bell's theorem

Device-independent quantum random number generation (DI-QRNG) is a groundbreaking approach to generating truly random numbers using the principles of quantum mechanics. Unlike traditional methods of generating random numbers, which rely on deterministic algorithms or physical processes, DI-QRNG uses the inherent randomness of entangled quantum systems to produce unpredictable and independent numbers that are not influenced by any particular experimental setup or device.

The key idea behind DI-QRNG is Bell's theorem, which states that any physical theory that obeys locality and realism (i.e., that assumes objects have definite properties when they are not being observed) must obey certain inequalities that can be violated by quantum mechanics. This violation implies that there is no local hidden variable theory that can fully explain the correlations between entangled quantum particles, and that their outcomes must be fundamentally unpredictable and random. In 2022, the Nobel Prize in Physics 2022 was awarded jointly to Alain Aspect, John F. Clauser and Anton Zeilinger "for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science". By using these measurements to generate random bits, DI-QRNG ensures that the generated numbers are completely independent of the measurement devices used to obtain them.

One of the main advantages of DI-QRNG over other methods of generating random numbers is its high level of security. Because the numbers are generated based on the fundamental laws of physics rather than on any specific algorithm, it is virtually impossible for an attacker to predict or manipulate the output. This makes DI-QRNG particularly useful in applications such as cryptography, where high-quality randomness is essential for maintaining the security of sensitive data.

Another advantage of DI-QRNG is that it does not require any assumptions about the properties of measurement devices, making it more robust against attacks that exploit vulnerabilities in hardware or software. In contrast, traditional QRNGs may be susceptible to flaws in the design or implementation of the physical systems used to generate random numbers. With DI-QRNG, however, the security of the generated random numbers is guaranteed by the laws of quantum mechanics themselves, making it a promising tool for a wide range of applications.

## Workflow of DI-QRNG

![](./README_pic/workflow.png)

## Randomness extraction and assessment

In information sicence, entropy is a metric that quantifies the level of randomness within a system, or conversely, the amount of information that can be obtained from it. 

The Shannon entropy, also referred to as a basic measure of randomness, provides an estimate of this quantity by indicating the average amount of information (in bits) that can be extracted or acquired from the system. Let $X$ be a random variable obeying the probability distribution $P(x)$, the Shannon entropy is defined as 

$$H(X)=-\sum_{x\in\chi}P(x)\log_2P(x)$$
in which, $\chi$ denotes the set of all possible values of $x$. However, the Shannon entropy is actually a upper bound to evaluate the randomness. 

The lower bound of entropy is determined by the min-entropy $H_\infty(X)$, which is defined as 

$$H_\infty(X)=-\log_2\left[\max_{x\in\chi}P(x)\right]$$

Knowing the amount of randomness, in realistic QRNG device, it's necessary to distill the true randomness from classical noise. An extractor is a mapping function from $\{0,1\}^n\times\{0,1\}^d\rightarrow\{0,1\}^m$, such that for every probability distribution $X$ on $\{0,1\}^n$ with $H_\infty(X)\ge k$, the probability function $\text{Ext}(X,U_d)$ is $\varepsilon$-close to the uniform distribution $\{0,1\}^m$. The $U_d$ represents a uniform distribution on $\{0,1\}^d$, and $\varepsilon$-close is an error parameter of similarity of different distributions.

In applications, the Toeplitz matrices are commonly used to extract the random numbers from raw outputs. According to [Leftover Hash Lemma](https://dl.acm.org/doi/10.1145/73007.73009), the Toeplitz-hashing extractor is a strong extractor, that is, the random seed $U_d$ can be reused for subsequent applications.

After randomness extract, [NIST testing suite](https://csrc.nist.gov/projects/random-bit-generation/documentation-and-software) is used to assess the quality of random numbers. See the [Appendix A](#appA) for the comparison between PRNG (produced by the NIST software) and QRNG (taken from the [public data](https://www.dropbox.com/sh/hae9ht1cc426i5g/AABcuGgGyuNJMC0zOxIhOQBGa?dl=0) of [2].

## Experimental realization on cloud quantum computers

In this section, we explain the experimental details and results to generate quantum random numbers, which are certified by Bell's theorem, using publicly cloud quantum computers.

### Clauser-Horne-ShimonyHolt (CHSH) game

CHSH game was proposed in paper [3], in which an inequality is used to discriminate the quantum mechanics from the local hidden-variable theories. Here, we empoly the same game settings as the paper [4]. In every trial, a Bell state is generated and distributed to two players, named Alice and Bob. The two players randomly select their measurements basis as $x_i\in\{0,1\}$ and $y_i\in\{0,1\}$. Then, the measurement outputs is denotes as $a_i, b_i$. The Bell value in single trial $i$ is calculated as

$$J_i=\begin{cases}
1,&\text{if}\quad a_i\bigoplus b_i=x_iy_i \\
0,&\text{others}
\end{cases}$$

and the CHSH game value is an average of $J_i$ for all trials, as

$$J=\sum_{i=1}^nJ_i-\frac34$$

here, $3/4$ is the classical threshold.

### Quantum circuits

TBD

### Results

TBD

### Discussions

TBD

## References

[1] Bruynsteen, Cédric, et al. "100-Gbit/s integrated quantum random number generator based on vacuum fluctuations." PRX Quantum 4.1 (2023): 010330.
[2] Liu, Wen-Zhao, et al. "Device-independent randomness expansion against quantum side information." Nature Physics 17.4 (2021): 448-451.
[3] Clauser, John F., et al. "Proposed experiment to test local hidden-variable theories." Physical review letters 23.15 (1969): 880.
[4] Liu, Yang, et al. "High-speed device-independent quantum random number generation without a detection loophole." Physical review letters 120.1 (2018): 010503.

<!--## Comparison between QRNG and VRF-->

## Appendix A
<span id='appA'> </span>

### PRNG NIST test
![](./README_pic/PRNG_1.png)
![](./README_pic/PRNG_2.png)

### QRNG NIST test
![](./README_pic/QRNG_1.png)
![](./README_pic/QRNG_2.png)


