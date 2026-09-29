---
title: 'OpenXLA Summer DevLab 2026 — Benchmarking vLLM on XLA Backends'
event: Google OpenXLA DevLab Summer 2026
location: Google Corporate HQ, Mountain View, CA
summary: 'Invited talk at Google OpenXLA DevLab Summer 2026 on "Benchmarking vLLM on XLA Backends: From CUDA to OpenXLA for LLM Serving", speaking alongside engineers from Google, NVIDIA, and Meta PyTorch.


  **Key points:**

  - Evaluating the production readiness of the matured vLLM + OpenXLA serving stack for enterprise LLM workloads

  - Why raw vendor peak-throughput curves mislead and how to measure true usable goodput under strict SLOs (TTFT ≤ 1000ms, TPOT ≤ 50ms)

  - Unpacking interconnect saturation: how multi-accelerator 70B tensor parallelism without NVLink collapses goodput from 9.3 to 2.4 req/s

  - The cold-start compilation penalty: why static XLA tensor bucketing creates a 20–30 minute ahead-of-time wall for uncompiled shapes

  - Deep dive into the 2026 unified stack: JetStream consolidation into `tpu-inference`, Torchax lowering, and Ragged Paged Attention v3 achieving up to 86% MBU


  **Takeaway:** Infrastructure decisions cannot rely on peak token throughput alone — single-variable benchmarking with fixed SLOs reveals that interconnect topologies and static compilation profiles govern production serving viability.'
abstract: 'Invited by Google''s ML and TPU teams to speak at DevLab Summer 2026 at Google HQ in Mountain View, CA. My talk, "Benchmarking vLLM on XLA Backends: From CUDA to OpenXLA for LLM Serving," covered our empirical findings comparing production serving paths across NVIDIA GPUs and Google TPUs.

  When evaluating enterprise migrations from GPUs to TPUs, traditional vendor benchmarks create a mirage by altering request shapes, dropping cold starts, or hiding compilation overhead. To cut through this, our team at PayPal AI Lab built an open-source, single-variable benchmark harness keeping weights, client semantics, request distributions, and SLOs strictly identical. We evaluate where the matured vLLM + OpenXLA stack excels, the impact of the systolic array compilation model on dynamic chat traffic, and the tail-latency collapse that occurs when multi-accelerator tensor collectives saturate PCIe interconnects.'
date: '2026-06-25T18:00:00Z'
date_end: '2026-06-25T19:30:00Z'
all_day: false
publishDate: '2026-06-26T00:00:00Z'
authors:
- admin
tags:
- OpenXLA
- TPU
- vLLM
- LLM Serving
- AI Systems
- Benchmarking
- Invited Talk
featured: false
links:
- name: Video
  url: https://www.youtube.com/watch?v=-AjLjr5kPqY
- name: Slides
  url: https://github.com/rabimba/vllm-xla-bench/blob/main/devlab-vllm-xla_talk%20.pdf
- name: Benchmark Code
  url: https://github.com/rabimba/vllm-xla-bench
- name: Deep-Dive Blog
  url: /blog/the-throughput-trap-benchmarking-vllm/
---

### Talk Overview

Invited by Google's ML and TPU teams to present at **OpenXLA Summer DevLab 2026** hosted at Google Corporate HQ in Mountain View, CA, alongside speakers from Google, NVIDIA, and the Meta PyTorch team.

The talk details our empirical evaluation of the matured **vLLM + OpenXLA** stack, contrasting it with the native **vLLM + CUDA** serving path under identical enterprise workloads.

---

### Key Technical Insights

#### 1. The Runtime Collision: Dynamic CUDA vs. Static OpenXLA
- **GPU / CUDA:** Inherently dynamic, memory allocation and kernel launches scale on the fly to arbitrary prompt lengths with near-instantaneous container startup.
- **TPU / OpenXLA:** Built around high-density **Systolic Arrays** streaming deterministic matrix multiplications. XLA compiles rigid machine code ahead of time, requiring incoming variable-length prompts to be mapped into static padding buckets (128, 256, 512, 1024 tokens), introducing compute padding overhead.
- **The Compilation Wall:** Uncompiled sequence configurations or cold starts trigger ahead-of-time compilation passes that can pause server execution for 20–30 minutes, complicating elastic autoscaling.

#### 2. The Throughput Trap vs. Usable Goodput
- Standard evaluations optimize for **Peak Throughput** (tokens/sec), masking degraded latency.
- LLM inference splits into:
  - **Prefill phase:** Compute-bound; dictates **Time to First Token (TTFT)**.
  - **Decode phase:** Memory-bandwidth-bound; dictates **Time Per Output Token (TPOT)**.
- We evaluate capacity using **Usable Goodput** — requests per second successfully meeting both **TTFT ≤ 1000 ms** and **TPOT ≤ 50 ms** simultaneously.

#### 3. Interconnect Limits & Tail Latency Collapse
- On single-chip configurations (e.g., Llama-3.1 8B), the system scales predictably, keeping P99 response loops under 38 ms.
- For partitioned 70B models requiring inter-chip all-reduce tensor collectives, operating over baseboard **PCIe Gen5 without NVLink bridges** quickly saturates the bus. P99 decode tail latency spikes to **~466 ms/token**, causing usable goodput to collapse from **9.3 down to 2.4 requests/second** under peak concurrency.

#### 4. The 2026 Unified vLLM-XLA Stack Architecture
- **Consolidated Control Layer:** Google's internal JetStream stack was officially archived in early 2026 and folded into the JAX-native `tpu-inference` engine, with vLLM providing the OpenAI-compatible frontend orchestrator.
- **Torchax Lowering:** Standard PyTorch graphs are caught on-the-fly and lowered into StableHLO structures without eager Python interpreter bottlenecks.
- **Ragged Paged Attention v3 (RPA v3):** Implemented in Google's low-level Pallas and Mosaic kernel layout engines, RPA v3 enables dynamic ragged tiling inside HBM, fusing KV-cache scatter steps into the attention block and delivering up to **86% Model Bandwidth Utilization (MBU)** during generation.

---

### Resources & Artifacts

- **Presentation Slides:** [devlab-vllm-xla_talk.pdf](https://github.com/rabimba/vllm-xla-bench/blob/main/devlab-vllm-xla_talk%20.pdf)
- **Benchmark Harness & Test Suite:** [github.com/rabimba/vllm-xla-bench](https://github.com/rabimba/vllm-xla-bench)
- **Deep-Dive Engineering Post:** [The Throughput Trap: Benchmarking vLLM on OpenXLA](/blog/the-throughput-trap-benchmarking-vllm/)
- **Recorded Session Stream:** [Watch on YouTube](https://www.youtube.com/watch?v=-AjLjr5kPqY)
