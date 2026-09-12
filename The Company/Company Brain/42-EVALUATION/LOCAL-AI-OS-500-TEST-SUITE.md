# LOCAL AI OS — 500-TEST MASTER SUITE

> **Scope:** Full System Verification for the Persistent Local AI Operating System
> **Authority:** 42-EVALUATION / System Architecture Control Plane (CP-027)

The principle is:
> **Nothing is considered complete because it is configured. It is complete only when the test produces evidence of working behavior.**

## Test Status Vocabulary
Use only:
* `PASS`
* `FAIL`
* `BLOCKED`
* `NOT_TESTED`
* `DEGRADED`
* `UNKNOWN`

**Recommended registry fields:**
`test_id | domain | component | test | machine | precondition | command/action | expected_result | actual_result | status | evidence | timestamp | remediation`

---

## 001–025 — Hardware & Machine Foundation
| # | Test |
| --: | --- |
| 001 | Mac Studio boots successfully |
| 002 | MacBook Air boots successfully |
| 003 | Studio CPU health verified |
| 004 | Air CPU health verified |
| 005 | Studio unified memory detected correctly |
| 006 | Air unified memory detected correctly |
| 007 | Studio GPU/Apple Silicon detected |
| 008 | Air GPU/Apple Silicon detected |
| 009 | Studio available disk space verified |
| 010 | Air available disk space verified |
| 011 | LaCie mount exists |
| 012 | T7 Shield mount exists |
| 013 | LaCie read test passes |
| 014 | LaCie write test passes |
| 015 | T7 read test passes |
| 016 | T7 write test passes |
| 017 | sustained Studio CPU test |
| 018 | sustained Studio memory test |
| 019 | sustained local inference test |
| 020 | Studio thermal behavior verified |
| 021 | Air thermal behavior verified |
| 022 | Studio sleep/wake recovery |
| 023 | Air sleep/wake recovery |
| 024 | Studio reboot recovery |
| 025 | Air reboot recovery |

## 026–050 — Storage & Filesystem
| # | Test |
| --: | --- |
| 026 | Canonical AI root exists |
| 027 | Model directory exists |
| 028 | Ollama storage directory exists |
| 029 | OmniRoute storage directory exists |
| 030 | GBrain storage directory exists |
| 031 | Neo4j storage directory exists |
| 032 | Qdrant storage directory exists |
| 033 | project directory exists |
| 034 | venture directory exists |
| 035 | agent directory exists |
| 036 | registry directory exists |
| 037 | log directory exists |
| 038 | backup directory exists |
| 039 | evaluation directory exists |
| 040 | cookbook directory exists |
| 041 | filesystem permissions verified |
| 042 | AI root survives reboot |
| 043 | files survive reboot |
| 044 | model files survive restart |
| 045 | database files survive restart |
| 046 | agent state survives restart |
| 047 | memory survives restart |
| 048 | storage corruption detection works |
| 049 | backup creation works |
| 050 | backup restoration works |

## 051–075 — Tailscale / Network
| # | Test |
| --: | --- |
| 051 | Tailscale installed on Studio |
| 052 | Tailscale installed on Air |
| 053 | Studio appears in tailnet |
| 054 | Air appears in tailnet |
| 055 | Studio reachable from Air |
| 056 | Air reachable from Studio |
| 057 | Studio Tailscale hostname resolves |
| 058 | Studio Tailscale IP resolves |
| 059 | Air can ping Studio |
| 060 | Studio can ping Air |
| 061 | Studio Ollama port reachable over tailnet |
| 062 | OmniRoute port reachable over tailnet |
| 063 | SSH reachable over tailnet |
| 064 | database ports remain private |
| 065 | unauthorized network access blocked |
| 066 | Tailscale reconnect after Wi-Fi change |
| 067 | Tailscale reconnect after sleep |
| 068 | Tailscale reconnect after reboot |
| 069 | latency Air→Studio measured |
| 070 | packet loss Air→Studio measured |
| 071 | large payload transfer succeeds |
| 072 | long-lived connection survives |
| 073 | dropped connection detected |
| 074 | dropped connection recovers |
| 075 | public internet exposure audit passes |

## 076–100 — SSH & Identity
| # | Test |
| --: | --- |
| 076 | Air SSH directory exists |
| 077 | Studio SSH directory exists |
| 078 | Air private key exists |
| 079 | Air public key exists |
| 080 | Studio private key exists |
| 081 | Studio public key exists |
| 082 | Air private-key permissions correct |
| 083 | Studio private-key permissions correct |
| 084 | `.ssh` permissions correct |
| 085 | `authorized_keys` permissions correct |
| 086 | Air SSH agent running |
| 087 | Studio SSH agent running |
| 088 | Air key loaded |
| 089 | Studio key loaded |
| 090 | Air→Studio SSH authentication |
| 091 | Studio→Air SSH authentication |
| 092 | Air→GitHub SSH authentication |
| 093 | Studio→GitHub SSH authentication |
| 094 | SSH config resolves correct identity |
| 095 | `IdentitiesOnly` behavior verified |
| 096 | Tailscale hostname SSH works |
| 097 | wrong-key rejection works |
| 098 | revoked-key rejection works |
| 099 | SSH survives reboot |
| 100 | Git clone/fetch/push through SSH works |

## 101–125 — GitHub / Repository Infrastructure
| # | Test |
| --: | --- |
| 101 | Git installed on Studio |
| 102 | Git installed on Air |
| 103 | GitHub authentication works |
| 104 | repository clone works |
| 105 | repository fetch works |
| 106 | repository pull works |
| 107 | repository push works |
| 108 | branch creation works |
| 109 | branch switching works |
| 110 | commit creation works |
| 111 | commit history preserved |
| 112 | uncommitted changes detected |
| 113 | dirty workspace warning works |
| 114 | rollback works |
| 115 | reset works |
| 116 | merge works |
| 117 | merge conflict detected |
| 118 | merge conflict recovery works |
| 119 | PR branch creation works |
| 120 | GitHub issue retrieval works |
| 121 | GitHub issue→task conversion works |
| 122 | repository registry matches actual repos |
| 123 | repository capability mapping verified |
| 124 | duplicate repository detection works |
| 125 | repository backup/recovery works |

## 126–150 — Ollama
| # | Test |
| --: | --- |
| 126 | Ollama installed on Studio |
| 127 | Ollama installed on Air |
| 128 | Ollama daemon starts |
| 129 | Ollama API responds |
| 130 | `/api/tags` responds |
| 131 | model listing works |
| 132 | model pull works |
| 133 | model delete works |
| 134 | model reload works |
| 135 | model unload works |
| 136 | model survives Ollama restart |
| 137 | Ollama survives Mac reboot |
| 138 | local API authentication boundary verified |
| 139 | basic generation works |
| 140 | streaming generation works |
| 141 | structured JSON generation works |
| 142 | long prompt works |
| 143 | system prompt works |
| 144 | coding prompt works |
| 145 | tool-call prompt works |
| 146 | concurrent request works |
| 147 | failed request returns recoverable error |
| 148 | malformed request handled correctly |
| 149 | Ollama logs captured |
| 150 | Ollama health check automated |

## 151–175 — Qwen Coding Models
| # | Test |
| --: | --- |
| 151 | Qwen3-Coder 30B exists |
| 152 | Qwen3-Coder 30B loads |
| 153 | Qwen3-Coder 30B unloads |
| 154 | Qwen3-Coder 30B reloads |
| 155 | Qwen3-Coder basic coding task |
| 156 | Qwen3-Coder code explanation |
| 157 | Qwen3-Coder function discovery |
| 158 | Qwen3-Coder bug identification |
| 159 | Qwen3-Coder bug fix |
| 160 | Qwen3-Coder feature implementation |
| 161 | Qwen3-Coder test generation |
| 162 | Qwen3-Coder test execution |
| 163 | Qwen3-Coder test repair |
| 164 | Qwen3-Coder repository understanding |
| 165 | Qwen3-Coder multi-file modification |
| 166 | Qwen3-Coder tool calling |
| 167 | Qwen3-Coder terminal workflow |
| 168 | Qwen3-Coder Git workflow |
| 169 | Qwen3-Coder long-context task |
| 170 | Qwen3-Coder context 4K |
| 171 | Qwen3-Coder context 8K |
| 172 | Qwen3-Coder context 16K |
| 173 | Qwen3-Coder context 32K |
| 174 | Qwen3-Coder context stress test |
| 175 | Qwen3-Coder failure/recovery test |

## 176–200 — Model Benchmarking
| # | Test |
| --: | --- |
| 176 | TTFT measurement |
| 177 | tokens/sec measurement |
| 178 | total latency measurement |
| 179 | memory consumption measurement |
| 180 | CPU utilization measurement |
| 181 | GPU utilization measurement |
| 182 | disk utilization measurement |
| 183 | 1-request benchmark |
| 184 | 2-request benchmark |
| 185 | 5-request benchmark |
| 186 | 10-request stress benchmark |
| 187 | short-context benchmark |
| 188 | medium-context benchmark |
| 189 | long-context benchmark |
| 190 | coding benchmark |
| 191 | reasoning benchmark |
| 192 | tool-use benchmark |
| 193 | JSON benchmark |
| 194 | repository benchmark |
| 195 | agent benchmark |
| 196 | Air vs Studio benchmark |
| 197 | Qwen7B vs Qwen30B benchmark |
| 198 | local vs cloud benchmark |
| 199 | cost-per-task benchmark |
| 200 | model selection benchmark |

## 201–225 — OmniRoute
| # | Test |
| --: | --- |
| 201 | OmniRoute installed |
| 202 | OmniRoute starts |
| 203 | OmniRoute health endpoint |
| 204 | `/v1/models` works |
| 205 | OpenAI-compatible endpoint works |
| 206 | local Ollama provider discovered |
| 207 | local MLX provider discovered |
| 208 | local llama.cpp provider discovered |
| 209 | provider registry populated |
| 210 | model registry populated |
| 211 | model routing works |
| 212 | coding model routing works |
| 213 | general model routing works |
| 214 | fallback routing works |
| 215 | provider failure triggers fallback |
| 216 | model failure triggers fallback |
| 217 | timeout triggers fallback |
| 218 | invalid provider handled |
| 219 | provider recovery detected |
| 220 | OmniRoute restart recovery |
| 221 | OmniRoute reboot recovery |
| 222 | Air→Studio OmniRoute request |
| 223 | authentication works |
| 224 | logs captured |
| 225 | routing decision recorded |

## 226–250 — OpenCode
| # | Test |
| --: | --- |
| 226 | OpenCode installed |
| 227 | OpenCode starts |
| 228 | OpenCode sees local model |
| 229 | OpenCode connects to OmniRoute |
| 230 | OpenCode uses Qwen3-Coder |
| 231 | OpenCode reads repository |
| 232 | OpenCode searches repository |
| 233 | OpenCode identifies relevant file |
| 234 | OpenCode edits file |
| 235 | OpenCode creates file |
| 236 | OpenCode deletes file safely |
| 237 | OpenCode runs terminal |
| 238 | OpenCode runs tests |
| 239 | OpenCode fixes failing test |
| 240 | OpenCode creates commit |
| 241 | OpenCode handles Git branch |
| 242 | OpenCode handles Git diff |
| 243 | OpenCode uses MCP |
| 244 | OpenCode switches models |
| 245 | OpenCode handles model failure |
| 246 | OpenCode resumes interrupted task |
| 247 | OpenCode completes multi-file task |
| 248 | OpenCode performs repo-wide task |
| 249 | OpenCode records evidence |
| 250 | OpenCode end-to-end coding task |

## 251–275 — OpenClaw
| # | Test |
| --: | --- |
| 251 | OpenClaw installed |
| 252 | OpenClaw starts |
| 253 | OpenClaw gateway works |
| 254 | OpenClaw session creation |
| 255 | OpenClaw session persistence |
| 256 | OpenClaw local model connection |
| 257 | OpenClaw OmniRoute connection |
| 258 | OpenClaw tool discovery |
| 259 | OpenClaw MCP connection |
| 260 | OpenClaw filesystem tool |
| 261 | OpenClaw terminal tool |
| 262 | OpenClaw GitHub interaction |
| 263 | OpenClaw agent task |
| 264 | OpenClaw multi-step task |
| 265 | OpenClaw long-running task |
| 266 | OpenClaw task interruption |
| 267 | OpenClaw task resumption |
| 268 | OpenClaw model fallback |
| 269 | OpenClaw session recovery |
| 270 | OpenClaw restart recovery |
| 271 | OpenClaw reboot recovery |
| 272 | OpenClaw permission boundary |
| 273 | OpenClaw secret protection |
| 274 | OpenClaw logs |
| 275 | OpenClaw end-to-end workflow |

## 276–300 — Hermes Agent
| # | Test |
| --: | --- |
| 276 | Hermes installed |
| 277 | Hermes starts |
| 278 | Hermes local model connection |
| 279 | Hermes OmniRoute connection |
| 280 | Hermes skill discovery |
| 281 | Hermes skill execution |
| 282 | Hermes persistent knowledge |
| 283 | Hermes conversation retrieval |
| 284 | Hermes task memory |
| 285 | Hermes tool calling |
| 286 | Hermes terminal execution |
| 287 | Hermes filesystem access |
| 288 | Hermes Git workflow |
| 289 | Hermes GitHub workflow |
| 290 | Hermes multi-step task |
| 291 | Hermes autonomous task |
| 292 | Hermes task interruption |
| 293 | Hermes task recovery |
| 294 | Hermes model fallback |
| 295 | Hermes restart recovery |
| 296 | Hermes reboot recovery |
| 297 | Hermes memory survives restart |
| 298 | Hermes identity survives restart |
| 299 | Hermes evidence recording |
| 300 | Hermes end-to-end workflow |

## 301–325 — OpenCoWork / Knowledge Work
| # | Test |
| --: | --- |
| 301 | OpenCoWork installed |
| 302 | OpenCoWork starts |
| 303 | sandbox initializes |
| 304 | sandbox isolation verified |
| 305 | filesystem tool works |
| 306 | terminal tool works |
| 307 | browser capability works |
| 308 | skill discovery works |
| 309 | MCP connection works |
| 310 | local model connection works |
| 311 | OmniRoute connection works |
| 312 | document workflow |
| 313 | research workflow |
| 314 | spreadsheet workflow |
| 315 | file transformation workflow |
| 316 | multi-step task |
| 317 | task interruption |
| 318 | task recovery |
| 319 | rollback works |
| 320 | destructive action protection |
| 321 | permission boundary |
| 322 | secret protection |
| 323 | state persistence |
| 324 | restart recovery |
| 325 | end-to-end knowledge workflow |

## 326–350 — GBrain / Company Brain
| # | Test |
| --: | --- |
| 326 | GBrain installed |
| 327 | GBrain starts |
| 328 | GBrain database initializes |
| 329 | memory write works |
| 330 | memory read works |
| 331 | memory survives restart |
| 332 | memory survives reboot |
| 333 | memory retrieval by keyword |
| 334 | semantic memory retrieval |
| 335 | entity retrieval |
| 336 | relationship retrieval |
| 337 | company retrieval |
| 338 | venture retrieval |
| 339 | person retrieval |
| 340 | project retrieval |
| 341 | decision retrieval |
| 342 | task retrieval |
| 343 | cross-agent memory |
| 344 | cross-machine memory |
| 345 | memory provenance |
| 346 | memory timestamp |
| 347 | conflicting-fact detection |
| 348 | stale-memory detection |
| 349 | memory backup/restore |
| 350 | GBrain end-to-end company-brain test |

## 351–375 — Neo4j / Knowledge Graph
| # | Test |
| --: | --- |
| 351 | Neo4j starts |
| 352 | Neo4j health check |
| 353 | database connection |
| 354 | node creation |
| 355 | relationship creation |
| 356 | node retrieval |
| 357 | relationship retrieval |
| 358 | venture→repo relationship |
| 359 | venture→capability relationship |
| 360 | repo→agent relationship |
| 361 | agent→tool relationship |
| 362 | agent→model relationship |
| 363 | venture→workflow relationship |
| 364 | company→venture relationship |
| 365 | person→company relationship |
| 366 | orphan-node detection |
| 367 | duplicate-node detection |
| 368 | missing-link detection |
| 369 | cluster detection |
| 370 | disconnected-space detection |
| 371 | over-connected-cluster detection |
| 372 | stale-edge detection |
| 373 | graph consistency test |
| 374 | graph backup/restore |
| 375 | graph survives reboot |

## 376–400 — Qdrant / Semantic Memory
| # | Test |
| --: | --- |
| 376 | Qdrant starts |
| 377 | Qdrant health |
| 378 | collection creation |
| 379 | vector insertion |
| 380 | vector retrieval |
| 381 | semantic search |
| 382 | metadata filtering |
| 383 | repository embeddings |
| 384 | venture embeddings |
| 385 | documentation embeddings |
| 386 | agent-memory embeddings |
| 387 | test-result embeddings |
| 388 | workflow embeddings |
| 389 | similarity accuracy |
| 390 | duplicate-vector detection |
| 391 | stale-vector detection |
| 392 | source attribution |
| 393 | timestamp attribution |
| 394 | cross-agent retrieval |
| 395 | cross-machine retrieval |
| 396 | restart persistence |
| 397 | reboot persistence |
| 398 | backup |
| 399 | restore |
| 400 | end-to-end semantic retrieval |

## 401–425 — MCP / Tool Bus
| # | Test |
| --: | --- |
| 401 | MCP runtime starts |
| 402 | MCP server discovery |
| 403 | MCP server connection |
| 404 | MCP authentication |
| 405 | MCP tool listing |
| 406 | MCP resource listing |
| 407 | MCP prompt listing |
| 408 | valid tool input |
| 409 | invalid tool input |
| 410 | missing argument handling |
| 411 | malformed argument handling |
| 412 | tool timeout |
| 413 | tool failure |
| 414 | tool retry |
| 415 | tool recovery |
| 416 | tool permission enforcement |
| 417 | filesystem MCP |
| 418 | GitHub MCP |
| 419 | database MCP |
| 420 | browser/search MCP |
| 421 | memory MCP |
| 422 | cross-agent MCP |
| 423 | MCP logging |
| 424 | MCP audit trail |
| 425 | end-to-end MCP workflow |

## 426–450 — Persistent Agent State & Cross-Machine Continuity
| # | Test |
| --: | --- |
| 426 | `SOUL.md` exists |
| 427 | `MISSION.md` exists |
| 428 | `MEMORY.md` exists |
| 429 | `GOALS.md` exists |
| 430 | `DECISIONS.md` exists |
| 431 | `STATE.json` exists |
| 432 | `RUNBOOK.md` exists |
| 433 | agent identity loads |
| 434 | agent mission loads |
| 435 | agent goals load |
| 436 | agent memory loads |
| 437 | agent state updates |
| 438 | state survives process restart |
| 439 | state survives reboot |
| 440 | task checkpoint created |
| 441 | task resumes from checkpoint |
| 442 | Studio starts task |
| 443 | Studio pauses task |
| 444 | Air retrieves task |
| 445 | Air continues task |
| 446 | Air updates state |
| 447 | Studio retrieves Air state |
| 448 | cross-machine memory synchronized |
| 449 | cross-machine Git state synchronized |
| 450 | complete Studio↔Air continuity test |

## 451–475 — Security, Reliability & Chaos
| # | Test |
| --: | --- |
| 451 | exposed-port scan |
| 452 | unauthorized Ollama access blocked |
| 453 | unauthorized OmniRoute access blocked |
| 454 | unauthorized SSH access blocked |
| 455 | database ports protected |
| 456 | API keys protected |
| 457 | `.env` files protected |
| 458 | SSH private keys protected |
| 459 | GitHub tokens protected |
| 460 | agent cannot read unauthorized secrets |
| 461 | agent filesystem boundary |
| 462 | agent destructive-action checkpoint |
| 463 | MCP permission boundary |
| 464 | log secret-leak scan |
| 465 | kill Ollama test |
| 466 | kill OmniRoute test |
| 467 | kill GBrain test |
| 468 | kill Qdrant test |
| 469 | kill Neo4j test |
| 470 | kill Docker test |
| 471 | kill Tailscale test |
| 472 | kill agent test |
| 473 | disconnect network test |
| 474 | recovery after all critical-service failures |
| 475 | full chaos/recovery test |

## 476–500 — Production, Business & Disaster Recovery
| # | Test |
| --: | --- |
| 476 | infrastructure health dashboard |
| 477 | model registry accuracy |
| 478 | agent registry accuracy |
| 479 | MCP registry accuracy |
| 480 | tool registry accuracy |
| 481 | SSH identity registry accuracy |
| 482 | infrastructure registry accuracy |
| 483 | workflow registry accuracy |
| 484 | test registry accuracy |
| 485 | repository registry accuracy |
| 486 | venture registry accuracy |
| 487 | automated health-check scheduler |
| 488 | automated benchmark scheduler |
| 489 | automated backup scheduler |
| 490 | automated graph-update loop |
| 491 | automated memory-update loop |
| 492 | venture research→prospect workflow |
| 493 | prospect→outreach workflow |
| 494 | outreach→CRM workflow |
| 495 | CRM→follow-up workflow |
| 496 | follow-up→quote workflow |
| 497 | quote→customer workflow |
| 498 | customer→delivery→invoice→payment workflow |
| 499 | destroy/rebuild Studio from source + backup |
| 500 | **FULL LOCAL AI OS END-TO-END TEST** |

---

## Test 500: The System Definition of Done

Test 500 proves the **entire system**.

```text
MacBook Air
     │
     │ Tailscale
     ▼
Mac Studio
     │
     ▼
OpenClaw
     │
     ▼
OmniRoute
     │
     ├── Ollama
     │      └── Qwen3-Coder 30B
     │
     ├── MLX
     ├── llama.cpp
     └── cloud fallback
     
     ├── OpenCode
     ├── Hermes
     ├── OpenCoWork
     │
     ├── MCP
     │
     ├── GBrain
     │      ├── Neo4j
     │      └── Qdrant
     │
     ├── GitHub
     │
     ├── Registries
     │
     └── Persistent Agent State
```

[[STARTHERE]] | [[INDEX]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[42-EVALUATION/README|Evaluation Hub]]
