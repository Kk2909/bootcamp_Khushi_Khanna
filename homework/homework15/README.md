\# Stage 15: Orchestration \& System Design



focuses on designing a pipeline orchestration plan.  

Key steps defined as tasks: \*\*ingest\_api → scrape\_aux → clean\_preprocess → feature\_engineer → model\_fit → evaluate\_report\*\*.  



\- Dependencies are represented as a DAG (with ingest/scrape running in parallel → clean → feature engineer → model → evaluate).  

\- Each task specifies \*\*inputs, outputs, logging, and checkpointing\*\*.  

\- A right-sizing decision is made: automate simple steps now (ingest, clean, model), keep DAG schedulers/manual orchestration out of scope.  



The deliverables are:  

&nbsp;`orchestration\_plan.md` 



Example run 

```bash

python -m src.orch.ingest\_step --ticker JPM --source yf



