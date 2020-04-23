# OptimalRDT Package
This package implements several advances in reliability demonstration test (RDT) design. 

- Multi-state RDT considering multiple test periods (Multi_State_I) and multiple failure modes (Multi_State_II). 
- RDT design considering acceptance decision uncertainty. 
- RDT design considering trade-offs from multiple objectives.

Version Update：
------
### Version 0.1.0
- Build classes of basic elements for optimal RDT design (e.g., Prior, Indicator, Core)
> Core is used to compute likelihood of failure probability, currently for multi-state RDT are built for two states (e.g., two periods, two failure modes)

### Version 0.2.0
- Build classes of different risk criteria (e.g, Consumer_Risk, Producer_Risk, Acceptance_Prob)
> Risk criteria for multi-state RDT are built for two states (e.g., two periods, two failure modes)

### Version 0.3.0
- Build classes of finding optimal RDT plan  based on minimum sample size(e.g., Optimal_Sample_Size)

### Version 0.4.0
- Build classes of Cost (e.g, RDT cost, warranty cost, reliability growth cost, expected overall cost)
> Expected cost is built only for Binomial RDT

- Build classes of finding optimal RDT plan  based on minimum cost and acceptance uncertainty(e.g., Optimal_Cost)
> Optimal_Cost is built only for Binomial RDT
