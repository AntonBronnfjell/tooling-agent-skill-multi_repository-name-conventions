# Repository Name Conventions

A practical guide for naming Git repositories consistently — whether you are an individual developer curating a portfolio, a freelancer juggling several clients, or an engineer inside a tiered enterprise with hundreds (or thousands) of repos to discover, secure, and govern.

The convention scales: small projects use only the core segments, while enterprise and client work layer optional prefixes and suffixes on top of the same base.

---

## TL;DR — The Pattern

**Core pattern (always required):**

```
<purpose>-<platform>-<repo-type>-<language>_<project-name>[.<project-module>]
```

**Full pattern (with optional enterprise / freelance / lifecycle segments):**

```
[<org>-][<scope>-][<client>-]<purpose>-<platform>-<repo-type>-<language>_<project-name>[.<project-module>][-<env>][-<region>][-<lifecycle>]
```

Rules at a glance:

- All lowercase. ASCII only. No spaces, no underscores inside a segment.
- Segments are separated by `-` (hyphen). The project name is separated from the technical prefix by `_` (underscore). Sub-modules use `.` (dot).
- Each segment uses a controlled vocabulary (see tables below). Avoid free-form words.
- Total length should fit on one terminal line — aim for **≤ 64 characters**, hard-cap at GitHub's 100.
- If a segment does not apply, omit it — do not insert placeholders like `none` or `xx`.

---

## The Core Segments

### 1. Purpose

Why the repository exists.

| Keyword    | Description                                                            |
| ---------- | ---------------------------------------------------------------------- |
| project    | Real-world app or service (website, API, full-stack application).      |
| product    | A commercial product owned by the org/business unit.                   |
| service    | A long-running backend service (often part of a microservice fleet).   |
| platform   | A foundational internal platform/PaaS layer used by other teams.       |
| client     | Work delivered for a specific external client (freelance/agency).      |
| challenge  | Coding problems, katas, algorithmic tasks, timed exercises.            |
| book       | Code written while following a book.                                   |
| course     | Practice or coursework (Coursera, Udemy, Pluralsight, YouTube, etc.).  |
| bootcamp   | Output from a bootcamp/intensive program.                              |
| hackathon  | Hackathon submissions or weekend builds.                               |
| workshop   | Hands-on session material (code + slides).                             |
| guide      | Educational repository that teaches or explains a concept.             |
| example    | Small illustrative demo or reference implementation.                   |
| template   | Boilerplate or scaffold for new projects.                              |
| starter    | Bootstrap kit — opinionated starter for a stack.                       |
| sandbox    | Experiments, drafts, feature flag spikes, non-finalised code.          |
| poc        | Proof of concept — small, throwaway, scoped to validate one question.  |
| prototype  | Early-stage exploratory build, slightly more polished than a PoC.      |
| mvp        | Minimum viable product — first shippable version of a new idea.        |
| research   | Academic, experimental, or paper-implementation repos.                 |
| spike      | Time-boxed technical investigation.                                    |
| migration  | Code/scripts to migrate from system A to system B.                     |
| config     | Centralised configuration (lint, prettier, ESLint, tsconfig, etc.).    |
| tooling    | Internal CLI tools, scripts, automation utilities.                     |
| docs       | Documentation-only repo (alternative to a `*-docs` suffix).            |
| license    | Software-licensing mechanisms or license metadata.                     |
| archive    | Legacy, deprecated, or frozen codebases kept for historical reference. |
| fork       | An intentional, long-lived fork of an upstream project.                |
| mirror     | A read-only mirror of an external source.                              |
| assets     | Non-code: icons, fonts, images, audio, video, brand assets.            |
| data       | Datasets, fixtures, seed data, reference data.                         |
| benchmark  | Performance benchmarks and comparison harnesses.                       |
| security   | Security tooling, threat models, hardening scripts.                    |
| compliance | Audit artifacts, policy-as-code, control evidence.                     |

### 2. Platform / Ecosystem

The primary technology, ecosystem, or learning source.

**Web frontends**

| Keyword    | Description                                                |
| ---------- | ---------------------------------------------------------- |
| react      | React.js                                                   |
| nextjs     | Next.js                                                    |
| remix      | Remix                                                      |
| astro      | Astro                                                      |
| svelte     | Svelte                                                     |
| sveltekit  | SvelteKit                                                  |
| vue        | Vue.js                                                     |
| nuxt       | Nuxt                                                       |
| angular    | Angular                                                    |
| solid      | SolidJS                                                    |
| qwik       | Qwik                                                       |
| htmx       | HTMX-based                                                 |
| alpine     | Alpine.js                                                  |

**Backends / runtimes**

| Keyword | Description                                            |
| ------- | ------------------------------------------------------ |
| nodejs  | Node.js                                                |
| deno    | Deno                                                   |
| bun     | Bun                                                    |
| dotnet  | .NET / C# ecosystem                                    |
| java    | Java (Spring, Jakarta EE)                              |
| kotlin  | Kotlin (Ktor, Spring + Kotlin)                         |
| python  | Python (Flask, Django, FastAPI)                        |
| ruby    | Ruby / Rails                                           |
| php     | PHP (Laravel, Symfony)                                 |
| go      | Go ecosystem                                           |
| rust    | Rust ecosystem                                         |
| elixir  | Elixir / Phoenix                                       |
| scala   | Scala                                                  |

**Mobile / desktop**

| Keyword   | Description                              |
| --------- | ---------------------------------------- |
| ios       | Native iOS / Swift                       |
| android   | Native Android (Kotlin/Java)             |
| flutter   | Flutter                                  |
| reactnative | React Native                           |
| expo      | Expo                                     |
| ionic     | Ionic / Capacitor                        |
| tauri     | Tauri                                    |
| electron  | Electron                                 |
| windows   | Windows-specific (WPF, UWP, PowerShell)  |
| macos     | macOS-specific (AppKit, SwiftUI native)  |
| linux     | Linux (distros, scripts, system-level)   |

**Cloud & infra**

| Keyword     | Description                                |
| ----------- | ------------------------------------------ |
| aws         | Amazon Web Services                        |
| azure       | Microsoft Azure                            |
| gcp         | Google Cloud Platform                      |
| oci         | Oracle Cloud Infrastructure                |
| do          | DigitalOcean                               |
| vercel      | Vercel                                     |
| netlify     | Netlify                                    |
| cloudflare  | Cloudflare (Workers, Pages, R2)            |
| supabase    | Supabase                                   |
| firebase    | Firebase                                   |
| heroku      | Heroku                                     |
| fly         | Fly.io                                     |
| kubernetes  | Kubernetes-specific                        |
| helm        | Helm charts                                |
| argocd      | Argo CD GitOps                             |
| terraform   | Terraform                                  |
| pulumi      | Pulumi                                     |
| ansible     | Ansible                                    |
| chef        | Chef                                       |
| puppet      | Puppet                                     |

**Embedded / hardware**

| Keyword    | Description                |
| ---------- | -------------------------- |
| arduino    | Arduino                    |
| esp32      | ESP32                      |
| esp8266    | ESP8266                    |
| raspi      | Raspberry Pi               |
| stm32      | STM32                      |

**Learning / content sources**

| Keyword     | Description |
| ----------- | ----------- |
| coursera    | Coursera    |
| pluralsight | Pluralsight |
| oreilly     | O'Reilly    |
| packt       | Packt       |
| udemy       | Udemy       |
| edx         | edX         |
| frontendmasters | Frontend Masters |
| youtube     | YouTube     |
| github      | GitHub features, actions, templates |

**AI agents / assistants**

The host that loads and runs the code. Use these when the repo's reason to exist is tied to a specific agent runtime.

| Keyword   | Description                                                              |
| --------- | ------------------------------------------------------------------------ |
| claude    | Claude, Claude Code, Claude Desktop (Anthropic).                         |
| chatgpt   | ChatGPT apps, GPTs, Codex (OpenAI).                                      |
| gemini    | Gemini, Gemini CLI, Jules (Google).                                      |
| copilot   | GitHub Copilot.                                                          |
| cursor    | Cursor.                                                                  |
| windsurf  | Windsurf.                                                                |
| cline     | Cline.                                                                   |
| aider     | Aider.                                                                   |
| zed       | Zed AI.                                                                  |
| continue  | Continue.dev.                                                            |
| amazonq   | Amazon Q Developer.                                                      |
| mcp       | Model Context Protocol — protocol-level, host-independent.               |
| agent     | Agent-agnostic — targets two or more hosts. See the "AI & Agent Repositories" section below. |

**AI / ML frameworks & runtimes**

| Keyword        | Description                                      |
| -------------- | ------------------------------------------------ |
| pytorch        | PyTorch                                          |
| tensorflow     | TensorFlow                                       |
| jax            | JAX                                              |
| sklearn        | scikit-learn                                     |
| huggingface    | Hugging Face (transformers, hub, spaces)         |
| langchain      | LangChain                                        |
| langgraph      | LangGraph                                        |
| llamaindex     | LlamaIndex                                       |
| crewai         | CrewAI                                           |
| autogen        | AutoGen                                          |
| dspy           | DSPy                                             |
| semantickernel | Semantic Kernel                                  |
| pydanticai     | Pydantic AI                                      |
| vercelai       | Vercel AI SDK                                    |
| mastra         | Mastra                                           |
| ollama         | Ollama (local inference)                         |
| vllm           | vLLM (serving)                                   |
| bedrock        | Amazon Bedrock                                   |
| vertexai       | Google Vertex AI                                 |
| azureopenai    | Azure OpenAI Service                             |
| openrouter     | OpenRouter                                       |
| litellm        | LiteLLM                                          |
| pinecone       | Pinecone (vector store)                          |
| weaviate       | Weaviate (vector store)                          |
| qdrant         | Qdrant (vector store)                            |
| chroma         | Chroma (vector store)                            |
| pgvector       | Postgres + pgvector                              |

**Data & analytics**

| Keyword       | Description                             |
| ------------- | --------------------------------------- |
| spark         | Apache Spark                            |
| databricks    | Databricks                              |
| snowflake     | Snowflake                               |
| bigquery      | Google BigQuery                         |
| redshift      | Amazon Redshift                         |
| dbt           | dbt transformations                     |
| airflow       | Apache Airflow                          |
| dagster       | Dagster                                 |
| prefect       | Prefect                                 |
| kafka         | Apache Kafka                            |
| flink         | Apache Flink                            |
| duckdb        | DuckDB                                  |
| clickhouse    | ClickHouse                              |
| postgres      | PostgreSQL                              |
| mysql         | MySQL / MariaDB                         |
| mongodb       | MongoDB                                 |
| redis         | Redis / Valkey                          |
| elasticsearch | Elasticsearch / OpenSearch              |
| neo4j         | Neo4j graph database                    |

**Testing & QA**

| Keyword    | Description                  |
| ---------- | ---------------------------- |
| playwright | Playwright                   |
| cypress    | Cypress                      |
| selenium   | Selenium                     |
| jest       | Jest                         |
| vitest     | Vitest                       |
| pytest     | pytest                       |
| junit      | JUnit                        |
| k6         | k6 load testing              |
| jmeter     | Apache JMeter                |
| gatling    | Gatling                      |
| locust     | Locust                       |

**Observability & security**

| Keyword       | Description                             |
| ------------- | --------------------------------------- |
| opentelemetry | OpenTelemetry instrumentation           |
| prometheus    | Prometheus                              |
| grafana       | Grafana dashboards / Loki / Tempo       |
| datadog       | Datadog                                 |
| sentry        | Sentry                                  |
| newrelic      | New Relic                               |
| splunk        | Splunk                                  |
| vault         | HashiCorp Vault                         |
| opa           | Open Policy Agent                       |
| keycloak      | Keycloak                                |
| auth0         | Auth0                                   |
| okta          | Okta                                    |
| semgrep       | Semgrep                                 |
| trivy         | Trivy                                   |

**Games, graphics & XR**

| Keyword  | Description                        |
| -------- | ---------------------------------- |
| unity    | Unity                              |
| unreal   | Unreal Engine                      |
| godot    | Godot                              |
| bevy     | Bevy (Rust)                        |
| threejs  | Three.js                           |
| webgl    | WebGL                              |
| webgpu   | WebGPU                             |
| webxr    | WebXR                              |
| visionos | Apple visionOS                     |
| quest    | Meta Quest                         |

**Web3 / blockchain**

| Keyword  | Description                      |
| -------- | -------------------------------- |
| ethereum | Ethereum / EVM chains            |
| solana   | Solana                           |
| polygon  | Polygon                          |
| cosmos   | Cosmos SDK                       |
| hardhat  | Hardhat toolchain                |
| foundry  | Foundry toolchain                |
| anchor   | Anchor (Solana framework)        |

**CMS, commerce & enterprise SaaS**

| Keyword     | Description                      |
| ----------- | -------------------------------- |
| wordpress   | WordPress                        |
| drupal      | Drupal                           |
| shopify     | Shopify                          |
| magento     | Adobe Commerce / Magento         |
| contentful  | Contentful                       |
| sanity      | Sanity                           |
| strapi      | Strapi                           |
| payload     | Payload CMS                      |
| directus    | Directus                         |
| salesforce  | Salesforce                       |
| sap         | SAP                              |
| dynamics    | Microsoft Dynamics               |
| servicenow  | ServiceNow                       |
| hubspot     | HubSpot                          |
| netsuite    | NetSuite                         |

**Third-party APIs & integration targets**

| Keyword  | Description                            |
| -------- | -------------------------------------- |
| stripe   | Stripe                                 |
| paypal   | PayPal                                 |
| twilio   | Twilio                                 |
| sendgrid | SendGrid / Resend-class email APIs     |
| slack    | Slack                                  |
| discord  | Discord                                |
| telegram | Telegram                               |
| whatsapp | WhatsApp Business                      |
| teams    | Microsoft Teams                        |
| jira     | Jira / Atlassian                       |
| notion   | Notion                                 |
| obsidian | Obsidian                               |
| figma    | Figma                                  |
| vscode   | Visual Studio Code                     |
| chrome   | Chrome / Chromium extensions           |
| firefox  | Firefox extensions                     |
| zapier   | Zapier / n8n-class automation          |

### 3. Repository Type

The shape and architecture of the codebase.

| Keyword       | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| web           | Frontend (SPA, MPA, SSR, SSG).                               |
| api           | REST / GraphQL / gRPC API.                                   |
| service       | Long-running backend service.                                |
| microservice  | A single service inside a microservice fleet.                |
| worker        | Background worker / queue consumer.                          |
| cronjob       | Scheduled batch job.                                         |
| function      | Serverless function (Lambda, Cloud Functions, Workers).      |
| gateway       | API gateway / BFF.                                           |
| proxy         | Reverse proxy / sidecar.                                     |
| bot           | Chat bot, Discord/Slack bot, automation bot.                 |
| scraper       | Web scraper / data ingestion crawler.                        |
| etl           | ETL / ELT data pipeline.                                     |
| pipeline      | Generic data or ML pipeline.                                 |
| stream        | Streaming/event-processing app (Kafka, Kinesis, Pulsar).     |
| app           | Mobile/desktop application.                                  |
| mobile        | Mobile-specific (iOS, Android, hybrid).                      |
| desktop       | Desktop application.                                         |
| pwa           | Progressive Web App.                                         |
| container     | Docker / container build infrastructure.                     |
| infra         | Generic infrastructure-as-code.                              |
| cloud         | Cloud-specific IaC (Terraform, Pulumi, CDK).                 |
| devops        | CI/CD pipelines, observability, release tooling.             |
| gitops        | GitOps configuration (Argo CD, Flux).                        |
| test          | Test suites (unit, integration, E2E).                        |
| e2e           | End-to-end test harness only.                                |
| data          | SQL scripts, schemas, datasets, dbt models.                  |
| ml            | Machine learning.                                            |
| ai            | AI agents, LLM apps, prompt suites.                          |
| embedsyst     | Embedded systems / IoT firmware.                             |
| firmware      | Device firmware.                                             |
| driver        | Hardware/software driver.                                    |
| shell         | Bash / ZSH / CMD scripts.                                    |
| cli           | Command-line tool.                                           |
| sdk           | Client SDK for an API or platform.                           |
| lib           | Library / package.                                           |
| framework     | Reusable framework.                                          |
| package       | Distributable package (npm, PyPI, NuGet, crates).            |
| plugin        | Plugin / extension (WordPress, VSCode, Figma, Obsidian).     |
| skill         | Agent skill — instructions plus optional scripts loaded by an AI host. |
| agentdef      | Agent definition itself (persona, tool wiring, orchestration graph).    |
| mcpserver     | MCP server exposing tools, resources, or prompts.                      |
| mcpclient     | MCP client / host implementation.                                      |
| hook          | Event-triggered scripts (git, agent lifecycle, CI, inbound webhooks).  |
| command       | Slash commands or custom prompt commands for an agent.                 |
| prompt        | Prompt library, system-prompt collection, prompt templates.            |
| eval          | Evaluation harness scoring non-deterministic model or agent output.    |
| rag           | Retrieval-augmented generation app: ingestion, indexing, retrieval.    |
| finetune      | Fine-tuning, LoRA, or model-adaptation pipelines.                      |
| guardrail     | Safety filters, moderation, policy enforcement around a model.         |
| theme         | UI theme / skin.                                             |
| integration   | Middleware / system connector.                               |
| monorepo      | Multi-package / multi-app monorepo (Nx, Turborepo, pnpm).    |
| dashboard     | Admin or monitoring dashboard.                               |
| portal        | Customer or internal portal.                                 |
| docs-site     | Hosted documentation site.                                   |
| browserext    | Browser extension (Chrome, Firefox, Safari).                 |
| daemon        | Long-running system daemon or host agent process.            |
| game          | Game or interactive experience.                              |
| engine        | Game, render, or simulation engine.                          |
| shader        | Shader packs and GPU pipelines.                              |
| simulator     | Simulator or emulator.                                       |
| compiler      | Compiler, transpiler, or language toolchain.                 |
| parser        | Parser, lexer, linter, or formatter.                         |
| protocol      | Protocol or specification definition.                        |
| schema        | Schema / contract repo (OpenAPI, protobuf, Avro, JSON Schema). |
| designsys     | Design system or component library.                          |
| loadtest      | Load and performance test harness.                           |
| chaos         | Chaos and resilience experiments.                            |
| observability | Dashboards, alerts, and SLOs as code.                        |
| contract      | On-chain smart contracts.                                    |
| dapp          | Decentralised app (contracts plus frontend).                 |
| notebook      | Notebook-driven analysis or tutorial.                        |

### 4. Language

The primary language or canonical file format.

| Keyword     | Description                                          |
| ----------- | ---------------------------------------------------- |
| javascript  | JavaScript (client or server).                       |
| typescript  | TypeScript.                                          |
| python      | Python.                                              |
| csharp      | C#.                                                  |
| java        | Java.                                                |
| kotlin      | Kotlin.                                              |
| swift       | Swift.                                               |
| dart        | Dart.                                                |
| go          | Go.                                                  |
| rust        | Rust.                                                |
| cpp         | C++.                                                 |
| c           | C.                                                   |
| ruby        | Ruby.                                                |
| php         | PHP.                                                 |
| scala       | Scala.                                               |
| elixir      | Elixir.                                              |
| haskell     | Haskell.                                             |
| lua         | Lua.                                                 |
| r           | R.                                                   |
| julia       | Julia.                                               |
| solidity    | Solidity (smart contracts).                          |
| bash        | Bash scripts.                                        |
| zsh         | ZSH scripts.                                         |
| powershell  | PowerShell.                                          |
| dos         | Windows `.bat` / `.cmd`.                             |
| sql         | SQL.                                                 |
| html        | HTML-centric content repos.                          |
| css         | CSS / SCSS / Sass-centric.                           |
| markdown    | Markdown docs or static pages.                       |
| yaml        | YAML-focused (GitHub Actions, Kubernetes, Ansible).  |
| json        | JSON-focused (schemas, configs, APIs).               |
| toml        | TOML-focused configs.                                |
| hcl         | Terraform / HashiCorp HCL.                           |
| dockerfile  | Dockerfile-centric.                                  |
| graphql     | GraphQL schema/spec-centric.                         |
| protobuf    | Protocol Buffers / gRPC contracts.                   |
| multi       | Multi-language repository.                           |
| english     | Written in English (content repos).                  |
| spanish     | Written in Spanish (content repos).                  |
| mdx         | MDX (Markdown + components).                         |
| jupyter     | Jupyter notebooks.                                   |
| objectivec  | Objective-C.                                         |
| zig         | Zig.                                                 |
| nim         | Nim.                                                 |
| ocaml       | OCaml.                                               |
| erlang      | Erlang.                                              |
| clojure     | Clojure / ClojureScript.                             |
| fsharp      | F#.                                                  |
| vb          | Visual Basic / VBA.                                  |
| groovy      | Groovy (Gradle, Jenkins).                            |
| perl        | Perl.                                                |
| matlab      | MATLAB.                                              |
| assembly    | Assembly.                                            |
| verilog     | Verilog.                                             |
| vhdl        | VHDL.                                                |
| glsl        | GLSL / HLSL shader code.                             |
| gdscript    | GDScript (Godot).                                    |
| apex        | Salesforce Apex.                                     |
| abap        | SAP ABAP.                                            |
| wasm        | WebAssembly.                                         |
| nix         | Nix expressions.                                     |
| rego        | Rego (Open Policy Agent).                            |
| jsonnet     | Jsonnet.                                             |
| cue         | CUE.                                                 |
| starlark    | Starlark (Bazel, Buck).                              |
| make        | Makefiles.                                           |
| cmake       | CMake.                                               |
| latex       | LaTeX.                                               |
| xml         | XML-centric.                                         |
| csv         | CSV / TSV data files.                                |
| kql         | Kusto Query Language.                                |
| promql      | PromQL.                                              |
| cypher      | Cypher (Neo4j).                                      |

### 5. Project Name

The specific repo identity — kebab-case, descriptive, ≤ 30 characters where possible.

Optional suffixes give a quick read on the repo's role within a larger project family:

| Suffix       | Description                                                           |
| ------------ | --------------------------------------------------------------------- |
| `*-docs`     | Documentation accompanying a project.                                 |
| `*-api`      | API that pairs with another project (e.g., `portfolio-api`).          |
| `*-web`      | Web frontend for a project family.                                    |
| `*-mobile`   | Mobile client for a project family.                                   |
| `*-admin`    | Admin/back-office interface.                                          |
| `*-cli`      | Companion CLI.                                                        |
| `*-sdk`      | Companion SDK.                                                        |
| `*-worker`   | Background worker for the same product.                               |
| `*-infra`    | Infrastructure for the same product (usually cloud IaC).              |
| `*-installer`| Installer / bootstrap script.                                         |
| `*-demo`     | Demo-only deployment.                                                 |
| `*-starter`  | Starter kit / boilerplate.                                            |
| `*-test`     | Test suite / automated test tooling.                                  |
| `*-e2e`      | End-to-end test harness.                                              |
| `*-bench`    | Performance benchmarks.                                               |
| `*-fixtures` | Test or seed data.                                                    |

### 6. Project Module (optional)

For monorepos, microservice families, or multi-package products. Separated by `.` (dot).

```
project-react-web-typescript_mysaas.auth
project-nodejs-api-typescript_mysaas.payments
project-nodejs-worker-typescript_mysaas.emails
```

For deeper nesting (rarely needed), allow a second dot:

```
project-nodejs-api-typescript_mysaas.payments.invoicing
```

---

## AI & Agent Repositories

AI tooling has its own repo shapes — skills, MCP servers, hooks, slash commands, agent definitions, evals, RAG pipelines. They tend to be small, numerous, and fast-moving, which makes disciplined naming matter more rather than less: forty two-file repos are unreadable without structure.

### Agent skills

An **agent skill** is a folder of instructions — `SKILL.md`, `AGENTS.md`, `.cursor/rules/`, `.github/copilot-instructions.md` — plus optional scripts, loaded by an AI agent at runtime. It is a plugin in shape but prose in substance, so it gets its own repo type (`skill`) and takes the agent as its platform.

#### Single-agent skills

```
<purpose>-<agent>-skill-<language>_<skill-name>
```

```
tooling-claude-skill-markdown_invoice-parser
tooling-cursor-skill-markdown_react-conventions
tooling-copilot-skill-markdown_commit-messages
tooling-gemini-skill-python_repo-auditor
product-claude-skill-multi_contract-review
example-cursor-skill-markdown_rules-starter
guide-agent-skill-markdown_prompt-patterns
```

Rules:

- Name a specific agent only when the skill genuinely cannot run elsewhere — it depends on that host's file layout, tool APIs, or frontmatter schema. If it is portable prose, it is not a `claude` skill, it is an `agent` skill.
- `<language>` is `markdown` for instructions-only skills and `multi` when executable `scripts/` ship alongside. Use a concrete language (`python`, `bash`) only when the code is the substance and the prose is a thin wrapper around it.
- Skill names follow the project-name rules: kebab-case, descriptive, ≤ 30 characters. Do not repeat the agent inside the name — `claude-skill-markdown_claude-invoice-parser` says it twice.
- `<purpose>` is usually `tooling`. Reach for `product` if you sell it, `example` or `guide` if it exists to teach the pattern, `template` or `starter` if it is a scaffold for writing other skills.

#### Multi-agent skills

When one repository targets two or more hosts, use the `agent` keyword instead of stacking host names:

```
tooling-agent-skill-markdown_invoice-parser
```

Do **not** write `tooling-claude-cursor-copilot-skill-markdown_invoice-parser`. The list only grows, the name churns every time support is added or dropped, and it breaks the one-keyword-per-segment rule. Declare supported hosts in the repo `description` and `topics` — metadata is cheap to change, names are not.

Per-host adapters inside a multi-agent repo use the module segment:

```
tooling-agent-skill-markdown_invoice-parser.claude
tooling-agent-skill-markdown_invoice-parser.cursor
tooling-agent-skill-markdown_invoice-parser.copilot
```

A collection of many skills is a monorepo like any other:

```
tooling-agent-monorepo-multi_skills-library
tooling-agent-monorepo-multi_skills-library.invoice-parser
tooling-agent-monorepo-multi_skills-library.contract-review
```

Both forms pass the existing validation regexes unchanged.

### MCP servers and clients

An MCP server exposes tools, resources, or prompts over the Model Context Protocol, and any compliant host can call it. That host-independence is the whole point, so the platform segment is `mcp` — not whichever agent you happened to test against.

```
tooling-mcp-mcpserver-typescript_github-issues
tooling-mcp-mcpserver-python_snowflake-reader
tooling-mcp-mcpclient-typescript_desktop-bridge
tooling-mcp-lib-typescript_server-sdk
acme-data-platform-service-mcp-mcpserver-go_warehouse-tools-tier1-pii
```

- Name a host (`claude`, `cursor`) only for a server that genuinely cannot run anywhere else — a bundled, host-specific extension rather than a standalone server.
- Transport does not belong in the name. stdio today, streamable HTTP tomorrow; put it in the README.
- A remotely hosted, multi-tenant server is a production service and earns the enterprise suffixes (`-tier1`, `-pii`, `-soc2`) like anything else.
- Wrapping a third-party API is still `mcpserver`, not `integration` — the protocol is the defining trait, not the thing behind it.

### Hooks

A `hook` fires on someone else's event: a git lifecycle event, an agent tool call, a CI stage, an inbound webhook.

```
tooling-git-hook-bash_commit-guards
tooling-claude-hook-python_pretooluse-audit
tooling-agent-hook-bash_secret-scan-gate
tooling-github-hook-yaml_org-webhook-router
```

When the shape is ambiguous, classify by what pulls the trigger:

| Trigger                                          | Repo type |
| ------------------------------------------------ | --------- |
| Another system's lifecycle event                 | hook      |
| A clock                                          | cronjob   |
| An HTTP or cloud event, deployed serverless      | function  |
| A queue message                                  | worker    |
| A long-running listener you operate              | service   |

A webhook *receiver* you deploy and keep running is a `service`. A script the platform executes on your behalf is a `hook`.

### Commands, prompts, and agent definitions

```
tooling-claude-command-markdown_release-workflow
tooling-agent-command-markdown_review-commands
tooling-agent-prompt-markdown_system-prompt-library
project-claude-agentdef-markdown_support-triage
project-langgraph-agentdef-python_research-crew
project-agent-agentdef-python_ops-fleet.planner
project-agent-agentdef-python_ops-fleet.executor
```

Sub-agents in a fleet are modules of the fleet, not separate repos — until they get separate owners or separate release cycles, which is the same test you would apply to any microservice split.

### LLM applications, evals, and RAG

```
project-langchain-ai-python_support-copilot
project-pgvector-rag-python_docs-assistant
tooling-agent-eval-python_skill-regressions
research-pytorch-finetune-python_domain-adapter
tooling-agent-guardrail-python_output-filters
acme-ml-platform-service-vllm-service-python_inference-gateway-tier1
```

`eval` is deliberately separate from `test` and `benchmark`: tests assert deterministic behaviour, benchmarks measure speed, evals score non-deterministic output. They have different failure modes and usually different owners, so they should be greppable apart.

### Choosing the right repo type

| Repo shape                                                        | Repo type        | Platform             |
| ----------------------------------------------------------------- | ---------------- | -------------------- |
| Instructions plus optional scripts loaded into an agent's context | skill            | the agent, or `agent` |
| Packaged extension for an editor or app via a stable host API     | plugin           | vscode, obsidian, …  |
| A server exposing tools over MCP to any compliant client          | mcpserver        | mcp                  |
| A host-side implementation that consumes MCP servers              | mcpclient        | mcp, or the host     |
| A script another system triggers on an event                      | hook             | the triggering system |
| A reusable prompt or slash command                                | command, prompt  | the agent, or `agent` |
| A scoring harness for model output                                | eval             | the agent or framework |
| A library that a skill's scripts import                           | lib              | the language ecosystem |
| The agent itself — persona, tool wiring, orchestration            | agentdef         | the agent, or `agent` |

> Rule of thumb: if the deliverable is prose that steers a model, it is a `skill`. If it is code the host executes through an extension API, it is a `plugin`. If it is a process that speaks a protocol, it is a `service`.

---

## Enterprise Extensions

These optional **prefixes** let large organisations enforce discovery, ownership, and governance across many repos. Apply them in this order, omitting any that do not apply:

```
<org>-<business-unit>-<team>-<purpose>-...
```

### 7. Organisation / Tenant Prefix

Useful when a GitHub/GitLab account hosts repos for multiple legal entities, holdings, or acquired subsidiaries.

| Pattern | Example                       | When to use                                                 |
| ------- | ----------------------------- | ----------------------------------------------------------- |
| `acme-` | `acme-project-nextjs-web-ts_portfolio` | The org owns multiple brands and you need top-level separation. |

### 8. Business Unit / Domain

For tiered enterprises that organise around domains (Domain-Driven Design) or business units.

| Keyword     | Description                                  |
| ----------- | -------------------------------------------- |
| `fin-`      | Finance / billing / payments domain.         |
| `risk-`     | Risk and fraud.                              |
| `hr-`       | HR / people systems.                         |
| `mkt-`      | Marketing.                                   |
| `sales-`    | Sales / CRM.                                 |
| `ops-`      | Operations / supply chain.                   |
| `legal-`    | Legal / compliance.                          |
| `eng-`      | Internal engineering platform.               |
| `data-`     | Data platform / analytics.                   |
| `ml-`       | ML platform.                                 |
| `sec-`      | Security platform.                           |

### 9. Team / Squad

When repos must be traceable to a single owning squad (helps with on-call routing and CODEOWNERS).

```
fin-payments-project-go-microservice-go_ledger.posting
^^^ ^^^^^^^^
domain  squad
```

Use the team's short slug. Keep it stable — renaming squads is more expensive than renaming people.

### 10. Service Criticality / Tier

For enterprises with explicit service tiers (SLO/SLA).

| Suffix     | Tier description                                       |
| ---------- | ------------------------------------------------------ |
| `-tier1`   | Customer-facing, revenue-impacting, 24/7 on-call.      |
| `-tier2`   | Important but not revenue-critical.                    |
| `-tier3`   | Internal tools, batch jobs, best-effort.               |
| `-tier4`   | Experimental, no SLO.                                  |

Place criticality near the project name so it survives `grep`/discovery:

```
fin-payments-service-go-microservice-go_ledger-tier1
```

### 11. Environment

Most teams deploy a single repo to many environments via CI, so an environment suffix in the **repo name** should be rare. Use it only for **environment-specific code** that genuinely cannot be shared (e.g., bootstrap scripts for a specific stage).

| Suffix       | Description                |
| ------------ | -------------------------- |
| `-prod`      | Production-only artifact.  |
| `-staging`   | Staging-only.              |
| `-dev`       | Dev sandbox-only.          |
| `-sandbox`   | Throwaway sandbox account. |

### 12. Region / Locale

For physically split deployments or data-residency boundaries.

| Suffix  | Description       |
| ------- | ----------------- |
| `-eu`   | EU region.        |
| `-us`   | US region.        |
| `-apac` | APAC region.      |
| `-cn`   | Mainland China.   |
| `-gov`  | Gov-cloud.        |

### 13. Compliance / Data Classification

Make sensitive repos visible at a glance, especially for code-scanning policies and access control.

| Suffix          | Description                                           |
| --------------- | ----------------------------------------------------- |
| `-pii`          | Contains/handles personally identifiable information. |
| `-phi`          | Protected health information (HIPAA).                 |
| `-pci`          | In PCI-DSS scope.                                     |
| `-soc2`         | Under SOC 2 controls.                                 |
| `-gdpr`         | Specifically subject to GDPR considerations.          |
| `-hipaa`        | HIPAA-regulated.                                      |
| `-restricted`   | Restricted internal access.                           |
| `-confidential` | Confidential per classification policy.               |
| `-public`       | Intentionally public-ready (OSS, marketing).          |

> Data-classification suffixes are **labels for humans**, not access controls. Pair them with org policy and branch protection — never rely on the name alone.

### 14. Lifecycle / Status

For repos with long lifespans, signal where they sit in their lifecycle so contributors do not waste time on dead code.

| Suffix         | Description                                                                |
| -------------- | -------------------------------------------------------------------------- |
| `-incubation`  | New, unstable, expect breaking changes.                                    |
| `-active`      | Stable, actively maintained (default — usually omitted).                   |
| `-maintenance` | Bug fixes only, no new features.                                           |
| `-deprecated`  | Slated for removal; do not build on top of this.                           |
| `-sunset`      | In active wind-down, with a retirement date.                               |
| `-archived`    | Read-only, frozen. Prefer the platform's "archive" flag where available.   |

---

## Freelance / Agency Extensions

Freelancers and agencies have a different shape of problem: many clients, many engagements, NDAs, and the need to keep client work cleanly separated from personal work.

### 15. Client Prefix

```
client-<client-slug>-<purpose>-<platform>-<repo-type>-<language>_<project-name>
```

- Use a short, stable client slug (e.g. `acme`, `northwind`, `globex`).
- For NDA-bound work, prefer an opaque alias (`client-c14`) and store the real mapping in a private vault note rather than in the repo name.
- Apply the rest of the convention as usual after the client segment.

| Pattern                                | Use case                                  |
| -------------------------------------- | ----------------------------------------- |
| `client-acme-project-nextjs-web-ts_storefront` | Acme's e-commerce storefront.       |
| `client-acme-docs-astro-web-markdown_storefront-docs` | Acme storefront's docs site. |
| `client-c14-project-php-web-php_legacy-rewrite` | NDA-aliased client engagement.    |

### 16. Engagement / Year (optional)

For freelancers who re-engage with the same client across multiple distinct contracts, add a year or engagement code so historical archives stay legible:

```
client-acme-2025-project-nextjs-web-ts_storefront
client-acme-q3-project-nodejs-api-ts_storefront-api
```

### 17. Personal vs Client Separation

If you keep personal and client work in the same Git host account, reserve **bare project names** (`project-…`, `course-…`, `sandbox-…`) for personal work, and always prefix client work with `client-`. That way a single sort puts everything in its right bucket.

---

## Validation

A reasonable regex covering the core pattern (without the optional enterprise/freelance prefixes):

```
^[a-z]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+_[a-z0-9]+(-[a-z0-9]+)*(\.[a-z0-9]+(-[a-z0-9]+)*){0,2}$
```

A looser regex that allows all the optional segments:

```
^([a-z0-9]+-){0,4}[a-z]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+_[a-z0-9]+(-[a-z0-9]+)*(\.[a-z0-9]+(-[a-z0-9]+)*){0,2}(-[a-z0-9]+){0,4}$
```

Wire either of these into a pre-creation hook (GitHub App, GitLab webhook, or a `gh repo create` wrapper) so policy is enforced at the source.

---

## Examples

### Personal / portfolio

```
project-nextjs-web-typescript_portfolio
project-aws-cloud-terraform_portfolio-infra
docs-astro-web-markdown_portfolio-docs
sandbox-linux-shell-bash_dotfile-scripts
guide-react-web-javascript_hooks-demo
challenge-nodejs-cli-typescript_advent-of-code-2025
course-pluralsight-api-csharp_clean-architecture
config-github-devops-yaml_actions-templates
```

### Freelance / agency

```
client-acme-project-nextjs-web-typescript_storefront
client-acme-project-nodejs-api-typescript_storefront-api
client-acme-docs-astro-web-markdown_storefront-docs
client-northwind-2025-project-flutter-mobile-dart_loyalty-app
client-c14-project-php-web-php_legacy-rewrite-restricted
```

### Tier-enterprise

```
acme-fin-payments-service-go-microservice-go_ledger-tier1
acme-fin-payments-service-go-microservice-go_ledger-tier1-eu
acme-fin-payments-service-go-microservice-go_ledger.posting-tier1
acme-data-platform-pipeline-python-etl-python_warehouse-loaders
acme-eng-platform-project-typescript-cli-typescript_internal-cli-tier2
acme-sec-security-tooling-go-cli-go_secret-scanner-restricted
acme-hr-people-service-java-api-java_directory-pii-soc2
acme-mkt-website-project-nextjs-web-typescript_marketing-site-public
acme-ops-infra-cloud-terraform-hcl_kubernetes-baseline-tier1
acme-fin-payments-archive-php-web-php_legacy-portal-deprecated
```

### AI and agent tooling

```
tooling-claude-skill-markdown_invoice-parser
tooling-agent-skill-markdown_invoice-parser.cursor
tooling-mcp-mcpserver-typescript_github-issues
tooling-claude-hook-python_pretooluse-audit
tooling-agent-command-markdown_review-commands
project-langgraph-agentdef-python_research-crew
project-pgvector-rag-python_docs-assistant
tooling-agent-eval-python_skill-regressions
acme-ml-platform-service-vllm-service-python_inference-gateway-tier1
```

### Other technology domains

```
project-unity-game-csharp_puzzle-prototype
project-chrome-browserext-typescript_tab-manager
project-ethereum-contract-solidity_escrow-vault
project-shopify-web-typescript_storefront-theme
tooling-opentelemetry-observability-yaml_service-slos
tooling-playwright-e2e-typescript_checkout-flows
data-dbt-pipeline-sql_warehouse-models
project-esp32-firmware-cpp_sensor-node
tooling-figma-plugin-typescript_token-sync
config-nix-infra-nix_workstation-baseline
```

### Monorepos and platform repos

```
acme-eng-platform-project-typescript-monorepo-typescript_design-system
acme-eng-platform-project-typescript-monorepo-typescript_design-system.tokens
acme-eng-platform-project-typescript-monorepo-typescript_design-system.react
acme-eng-platform-project-typescript-monorepo-typescript_design-system.docs
```

---

## Anti-Patterns

Things to avoid:

- **CamelCase or PascalCase** (`MyAwesomeRepo`) — breaks on case-insensitive filesystems and is hard to read with `ls`.
- **Underscores between segments** (`project_react_web`) — the underscore is reserved for the **project-name** boundary in this convention.
- **Year-as-prefix without context** (`2024-portfolio`) — sorts repos chronologically instead of by purpose. Put years inside the engagement segment instead.
- **Cryptic abbreviations** (`prj-rx-w-js_pf`) — the few characters saved cost everyone reading the repo list.
- **Personal nicknames** (`my-awesome-thing`, `magnum-opus`) — fine for a single hobby repo, painful at scale.
- **Stuffing a feature flag in the name** (`project-react-web-js_portfolio-new-design`) — branches and tags carry feature state; the repo name should not.
- **Renaming repos to reflect status** (`project-foo-v2`, `project-foo-final`) — bump versions/tags, do not fork-by-rename.
- **Embedding credentials, customer names, or ticket IDs** — credentials are obvious, customer names violate NDA for freelance work, ticket IDs go stale.

---

## Related Conventions

Repo naming is one piece of a larger consistency story. Pair this with:

- **Branch naming.** A common pattern is `<type>/<ticket>-<short-slug>` — e.g. `feat/ENG-1421-add-rate-limit`, `fix/ENG-1488-null-pointer`, `chore/bump-deps`. Types: `feat`, `fix`, `chore`, `docs`, `refactor`, `test`, `perf`, `ci`, `build`, `revert`, `hotfix`, `release`.
- **Tag / release naming.** Semantic versioning (`v1.4.2`, `v2.0.0-rc.1`) for libraries; calendar versioning (`2026.05.0`) for products with frequent independent releases. For monorepos, prefix tags with the module: `ledger@v1.4.2`.
- **Commit messages.** [Conventional Commits](https://www.conventionalcommits.org/) — `feat(payments): add idempotency keys`. Plays well with the `<purpose>` and `<project-module>` segments above.
- **CODEOWNERS.** Mirror the `<domain>-<team>` prefix into `.github/CODEOWNERS` so ownership is mechanical.

---

## Adopting This in an Existing Org

You almost never get a clean slate. A pragmatic rollout:

1. **Apply to all new repos** starting on a fixed date. Enforce with a pre-create hook.
2. **Audit existing repos** into three buckets: rename now (cheap), rename at next major version (medium), leave (high cost — internal/external integrations point at the old name).
3. **For renamed repos**, keep the old GitHub/GitLab redirect alive; do not delete and recreate.
4. **For repos you cannot rename**, add the convention in the `description` field and add it to the `topics`/`labels` so discovery still works.
5. **Wire CODEOWNERS, branch protection, and CI templates to read from segments** — once the name is structured, automation gets a lot easier (e.g. "every `*-tier1` repo must have two reviewers and a passing security scan").

---

> Naming conventions are a small investment for an outsized return on discoverability, ownership, and governance. The goal is not perfection — it is to make the *common case* obvious and the *exceptions* visible.
