<!-- repo: https://github.com/nikbearbrown/livingmodels_org | stars: 0 | updated: 2026-03-30T05:23:11Z -->

# Living Models

**Causal intelligence for the decisions that actually matter.**

[livingmodels.org](https://livingmodels.org) · [Substack](https://www.hypothetical.ai/)

---

## What This Is

Most analytics systems are built to describe the past. Living Models is built to reason about what happens when you change something.

A **Living Model** is a decision-support architecture defined by four properties:

- **Causal** — encodes mechanisms, not correlations; recommendations are expressed as estimated interventional effects P(Y | do(X)), not associations observed in historical data
- **Counterfactual** — can reason about what would have happened under conditions that did not occur, evaluating the cost of decisions not taken as rigorously as decisions that were
- **Continually updated** — maintains a live connection between incoming data and model parameters, so estimates reflect current conditions rather than a training set assembled at some prior date
- **Treatment-oriented** — output is a ranked list of interventions evaluated by expected causal effect, not a description or a prediction

This is not an upgrade to existing analytics infrastructure. It is a different kind of analytical object, asking different questions.

---

## The Problem

Judea Pearl's Ladder of Causation identifies three qualitatively distinct classes of question:

| Rung | Question | Tools |
|------|----------|-------|
| 1 — Association | What does the data show? | Dashboards, regression, ML |
| 2 — Intervention | What would happen if we acted? | Causal graphs, do-calculus, structural equations |
| 3 — Counterfactual | What would have happened if things had been different? | Structural Causal Models |

No rung is reachable by accumulating more data at the rung below. Most enterprise analytics — including most systems marketed as "AI" — operates entirely on rung one. J.C. Penney's 2012 pricing collapse is the canonical example: the data was correct, the inference was wrong, and no amount of additional observational data could have closed that gap. The company needed a different instrument.

Living Models is the attempt to build that instrument.

---

## The Standard Causal Workflow Is Backwards

In virtually every organization deploying causal AI today, a data science team builds the causal model and domain experts are brought in at the end to validate it. This is the wrong order — and the reason is mathematical, not procedural.

Multiple distinct causal structures can be perfectly consistent with the same observational data. Causal discovery algorithms (PC, GES, NOTEARS) return this ambiguity honestly as a Completed Partially Directed Acyclic Graph: directed edges where the data can say something, undirected edges where it cannot. What resolves the undirected edges is domain knowledge — specifically, the kind of knowledge that comes from fifteen or twenty years of operating inside a system.

The expert who builds the model controls what the organization can see. The standard workflow gives that authorship to the person furthest from the system being modeled. Living Models inverts the order: extract, then formalize. The statistician's role shifts from author to editor. The domain expert moves from reviewer to originator.

---

## Architecture

### The Knowledge Acquisition Tool

The core workflow is a structured expert interview that extracts implicit causal knowledge and converts it into a first-draft DAG suitable for algorithmic refinement. It runs in four phases:

**1. Variable Confirmation** (~10 min)
The system presents a candidate variable list derived from domain literature. The expert confirms, rejects, and renames. No graph structure is discussed yet. LLMs handle literature synthesis; the expert's role is curatorial.

**2. Edge Elicitation** (~20 min)
The system presents candidate relationships in temporal language — "which tends to move first?" rather than "which causes which?" — because experts orient edges more reliably this way. Cycles are detected and resolved through temporal probing without telling the expert their model is mathematically invalid.

**3. Interventional Disambiguation** (~10 min)
The system identifies the highest-stakes undirected edges in the emerging CPDAG and presents interventional probes to orient them. Example: *"If you held B constant through external intervention — locked it — would changes in A still be associated with changes in C?"* The expert doesn't need to understand why this question resolves the equivalence. They only need to answer it.

**4. Confidence Calibration** (~5 min)
Reference-class calibration questions, correction function applied to subsequent estimates, rough probability distributions attached to oriented edges.

**Output:** A partially directed graph with rough probability distributions — not a publication-ready causal model, but a structure sufficient for first-pass counterfactual scenarios and targeted data collection. Approximately 45 minutes from a prepared domain expert.

### Downstream Pipeline

```
Expert Interview
       │
       ▼
First-Draft DAG (CPDAG)
       │
       ▼
Automated Discovery Refinement (NOTEARS / PC / GES / FCI)
       │
       ▼
Parameterization (conditional distributions from data)
       │
       ▼
Counterfactual Engine (abduction → action → prediction)
       │
       ▼
Intervention Ranking (Expected Value of Intervention)
       │
       ▼
Executive Report (recommendation + evidence + assumptions + counterfactual)
```

### Multi-Agent Design

Different reasoning responsibilities are assigned to distinct agents operating against the same emerging graph:

- **Temporal agent** — validates that proposed causes precede proposed effects
- **Physical plausibility agent** — checks that claimed mechanisms do not violate domain constraints
- **Dependence agent** — cross-references the emerging graph against available data to flag edges inconsistent with observed conditional independencies
- **Bias interception agent** — detects collider topologies as they form and generates corrective probes before the expert commits to a wrong structure

---

## Key Concepts

**Do-Operator** — Pearl's notation for deliberate intervention. P(Y | do(X = x)) is the probability of outcome Y if we set X to x by action — structurally different from P(Y | X = x), the probability of Y given that we observe X equal to x in data. J.C. Penney had the second. They needed the first.

**Markov Equivalence** — Multiple DAGs can encode identical conditional independence relationships, making them statistically indistinguishable from observational data alone. For a graph with ten variables, the number of consistent structures can run into the thousands. Resolving equivalence requires either experimental intervention or domain knowledge. This project uses the latter.

**CPDAG** — Completed Partially Directed Acyclic Graph. The honest output of causal discovery algorithms: directed edges where the equivalence class agrees on direction, undirected edges everywhere else. The expert interview targets the undirected edges that matter most for the intended decision analysis.

**Expected Value of Intervention (EVI)** — The primary output metric. Product of reliability (frequency with which the intervention produces positive outcomes) and effect size (magnitude of improvement when it does). Compared against the counterfactual trajectory (what would have happened without the intervention) to produce a decision-relevant ranking.

**Unconfoundedness** — The identifying assumption that all variables influencing both the decision to intervene and the outcome are measured and included. This assumption is almost never perfectly satisfied. The Living Model architecture makes the violation explicit and surfaces it in the executive report rather than hiding it inside a confidence interval.

---

## What "Causal AI" Actually Means

The name is misleading. Causal AI does not discover causal structure from data. It uses machine learning to estimate the statistical adjustments required by human-specified causal models.

The division of labor is precise:

- **The human provides:** the causal question, the causal graph, the identification strategy
- **The ML provides:** flexible, accurate estimation of nuisance parameters — E[Y|X] and E[D|X] — the confounding adjustment problem

Double/Debiased Machine Learning (Chernozhukov et al.) is the core estimation framework: Neyman orthogonality ensures that first-order errors in nuisance estimates cancel out; cross-fitting prevents overfitting from creating spurious correlations. The result is valid inference on the causal parameter of interest even when nuisance parameters are estimated by black-box ML methods.

The ML amplifies the quality of the human causal reasoning it's built on. It does not replace it.

---

## What This Project Is Not

- **Not a dashboard.** Dashboards answer rung-one questions. This project is built for rungs two and three.
- **Not a predictive model.** Predictive models assume the future resembles the past. Strategy is the act of making the future different from the past. These require different tools.
- **Not automated causal discovery.** NOTEARS and PC are used as refinement tools downstream of the expert interview, not as replacements for it.
- **Not an echo chamber.** Internal teams prompted with LLMs tend to validate existing strategy. This architecture is explicitly designed to intercept confirmation bias before it propagates through the causal structure.

---

## Related Work

The Living Models architecture draws on and integrates:

- **Pearl (2000, 2018)** — *Causality* and *The Book of Why*: the mathematical foundation
- **Chernozhukov et al.** — Double/Debiased Machine Learning for causal effect estimation
- **Athey & Wager** — Causal forests and heterogeneous treatment effect estimation
- **Duflo** — "Economist as Plumber": the distance between a correct causal estimate and an effective intervention
- **Sheffield Elicitation Framework (SHELF)** — structured protocols for expert probability elicitation
- **Analysis of Competing Hypotheses (ACH)** — bias interception through disconfirmation
- **IDEA Protocol** — Investigate, Discuss, Estimate, Aggregate for group belief aggregation
- **NOTEARS** — continuous optimization for causal graph learning from data
- **FinCARE** — hybrid LLM + knowledge graph + NOTEARS achieving F1 improvement from 0.163 to 0.759

---

## Project Structure

```
living-models/
├── knowledge-acquisition/    # Expert interview system
│   ├── elicitation/          # Variable confirmation, edge elicitation, disambiguation
│   ├── bias-detection/       # Collider detection, cycle resolution, ACH layer
│   └── calibration/          # Linguistic probability mapping, reference-class calibration
├── graph/                    # DAG construction and validation
│   ├── cpdag/                # Markov equivalence resolution
│   └── discovery/            # NOTEARS / PC / GES refinement
├── estimation/               # Causal effect estimation
│   ├── dml/                  # Double Machine Learning
│   └── heterogeneous/        # Causal forests, CATE estimation
├── counterfactual/           # Abduction-action-prediction engine
├── reporting/                # Executive report generation
│   ├── narration/            # LLM-mediated plain-language output
│   └── visualization/        # Decision-oriented graph display
└── docs/                     # Living Models book (in progress)
```

---

## Current Status

The components required to build this system exist. The assembly is the project.

- [x] Theoretical architecture documented
- [x] Expert interview protocol specified (45-minute MVP)
- [ ] Knowledge Acquisition Tool (conversational layer)
- [ ] Live CPDAG enforcement during interview
- [ ] Multi-agent bias interception pipeline
- [ ] Automated interventional probe generation from arbitrary CPDAGs
- [ ] DML estimation layer
- [ ] Counterfactual engine
- [ ] EVI ranking and executive report output

---

## The Living Models Book

The full theoretical treatment is being developed publicly at [hypothetical.ai](https://www.hypothetical.ai/). The table of contents covers six parts: the problem with existing analytics, the mathematical foundations of causal reasoning, the Living Model architecture, applications of the Christensen and Damodaran frameworks as causal structures, strategic case studies, and the frontier problems (latent confounders, network interference, agentic causal systems).

Writing in public because private thinking produces private blind spots.

---

## Contributing

If you are working on causal knowledge elicitation, LLM-guided DAG construction, Markov equivalence resolution, or the organizational implementation of causal inference — and particularly if you have encountered the knowledge bottleneck in practice — open an issue or reach out.

The case studies are being built now. If this is the problem your organization is sitting on, this is the project to watch.

---

## License

MIT

---

*The data was never the problem. It was always the question.*

## Living Models Website

## Prerequisites

Before you begin, ensure you have the following installed on your system:

### Required Software
- **Node.js and npm**
  - Download from [Node.js official website](https://nodejs.org/)
  - Choose the LTS (Long Term Support) version
  - The installer includes both Node.js and npm

- **Git** (for version control)
  - Download from [Git's official website](https://git-scm.com/downloads)

### System Requirements
- Operating System: Windows, macOS, or Linux
- RAM: At least 4GB recommended
- Disk Space: At least 1GB free space
- Internet connection for downloading packages

### Installation by Operating System

#### Windows
1. Download and run the Node.js installer from [Node.js website](https://nodejs.org/)
2. Download and run the Git installer from [Git website](https://git-scm.com/downloads)
3. Restart your computer after installation

#### macOS
```bash
# Using Homebrew
brew install node
brew install git
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install nodejs npm
sudo apt install git
```

### Verifying Installation
After installation, verify that everything is set up correctly:
```bash
node --version
npm --version
git --version
```

## Getting Started

First, install dependencies:

```bash
npm install --legacy-peer-deps
```

then, run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

### Troubleshooting

If you encounter any issues during installation:

1. **npm install fails**
   - Clear npm cache: `npm cache clean --force`
   - Try using `--legacy-peer-deps` flag if there are dependency conflicts
   - Ensure you're using a compatible Node.js version

2. **Permission errors**
   - Windows: Run terminal as administrator
   - Mac/Linux: Use `sudo` for system-wide installations

3. **Network issues**
   - Check your internet connection
   - If behind a proxy, configure npm accordingly
   - Try using a different npm registry: `npm config set registry https://registry.npmjs.org/`

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
