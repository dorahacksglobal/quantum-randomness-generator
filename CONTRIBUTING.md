The project is coordinated by Dora Factory quantum experiments team, supervised by Eric Zhang. Bernard Liu investigated the DI-QRNG protocols following the papers in References section of README. In early stage of project, Si-Yu Chen conducted experiments using AWS Braket and tested some circuits, for example, the core.py which defines the CHSH game circuits. Bernard Liu completed the rest of the experiment, including quantum tomography, 1E5 shots experiments, randomness comparison, extraction and NIST tests, then summarized the experiments and results (see README.md). During the whole project, Paul Deng provided help to access to various QC services.

The Dora Factory engineering team is currently working on a frontend to allow users to experiment with the random nubmers. When it's ready, it will be available to everyone who's interested in trying out DI- quantum random numbers.

At this moment, we have already extracted device-independent random numbers from cloud super-conducting computers. The random numbers can be used in private use cases. There are some interesting challenges, mainly the following two:

1. Make DI-QRNG publicly verifiable (or as much as possible) to reduce the reliance on the trust of cloud computing provider's integrity. There are near-term ideas and long-term ideas (e.g. blind quantum computing) to solve this problem, we will post more thoughts over time.
2. Further reduce the cost of DI-QRNG and make it competitive comparing to traditional pseudo-random number generation approaches.

In addition, we posted [four bounties](https://unitaryhack.dev/projects/dora-factory-quantum-experiments) to this year's [unitaryHack](https://unitaryhack.dev). These bounties are related to our current experiment and its theoretical foundations. Contribution to these bounties will help improve the experiment. We welcome hackers from unitaryHack 23 to hack on these problems.

To contribute to these bounties, please leave a message under the corresponding issue, and start working on it. Submit solutions and results with a pull request before the hackathon's end date. We strongly encourage hackers to submit a few days before the hackathon ends, so that we have time to review and interact with you. There might be multiple hackers working on a same bounty, in such case, we might split the bounties and assign bounty to multiple hackers.

If you have any questions, feel free to reach out to us on GitHub, we will respond as soon as possible.

Happy hacking!
