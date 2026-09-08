# Tiers 5 & 6: Cybersecurity & Zero Trust + FinTech, Commerce & Monetization
# CAP-141 to CAP-210

TIER_5_AND_6 = [
    # Tier 5: Cybersecurity & Zero Trust Architecture (CAP-141 to CAP-175)
    (
        "CAP-141", "Enterprise Identity & Access Management (IAM)",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Centralize user directories, single sign-on (SSO), and role-based directory permissions across enterprise services.",
        ["Employees retaining access to internal tools after offboarding", "Fragmented credentials across dozens of unmanaged SaaS tools", "Failure in enterprise customer security evaluations requiring SAML/SCIM"],
        ["Okta", "Keycloak", "Google Workspace IAM", "Authentik", "Ory Kratos"],
        ["CAP-002", "CAP-003", "CAP-142", "CAP-160"],
        ["iam", "sso", "saml", "scim", "identity"]
    ),
    (
        "CAP-142", "Zero Trust Network Architecture (ZTNA)",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Enforce strict identity-authenticated, micro-segmented network access without trusting perimeter firewalls.",
        ["Lateral movement by attackers across corporate networks following a single workstation breach", "Vulnerabilities associated with legacy, unsegmented corporate VPN appliances", "Exposure of internal admin portals to the public internet"],
        ["Tailscale", "Cloudflare Zero Trust", "Zscaler ZTNA", "WireGuard", "Pomerium"],
        ["CAP-021", "CAP-141", "CAP-143", "CAP-173"],
        ["zero-trust", "tailscale", "ztna", "wireguard", "microsegmentation"]
    ),
    (
        "CAP-143", "Mutual TLS (mTLS) & Service Identity",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Cryptographically authenticate and encrypt all service-to-service communications with rotating x509 certificates.",
        ["Unencrypted plaintext communications between internal database and app servers", "Man-in-the-middle packet sniffing within shared cloud network fabrics", "Impersonation of internal backend services by rogue pods"],
        ["SPIRE / SPIFFE", "Cert-Manager", "Istio mTLS", "Step-CA", "HashiCorp Vault PKI"],
        ["CAP-010", "CAP-022", "CAP-142", "CAP-157"],
        ["mtls", "spiffe", "spire", "certificates", "encryption"]
    ),
    (
        "CAP-144", "Web Application Firewall (WAF) & L7 Defense",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Inspect and filter incoming HTTP traffic to block SQLi, XSS, automated scraping, and known exploit payloads.",
        ["Zero-day web vulnerabilities exploited before developers can ship patches", "Malicious botnets scraping proprietary pricing and content catalogs", "Brute-force credential stuffing overwhelming authentication endpoints"],
        ["Cloudflare WAF", "AWS WAF", "ModSecurity / Coraza", "Fastly Next-Gen WAF", "Wallarm"],
        ["CAP-027", "CAP-028", "CAP-124", "CAP-145"],
        ["waf", "cloud-security", "coraza", "owasp", "l7-defense"]
    ),
    (
        "CAP-145", "Distributed Denial of Service (DDoS) Mitigation",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Absorb and scrub volumetric Layer 3/4 and Layer 7 distributed denial-of-service traffic attacks.",
        ["Complete application outages during extortionist DDoS attacks", "Skyrocketing cloud bandwidth and auto-scaling compute bills during traffic floods", "Degraded global performance for legitimate customers"],
        ["Cloudflare Magic Transit", "AWS Shield", "Fastly DDoS Protection", "Akamai Prolexic", "SYN Cookies"],
        ["CAP-027", "CAP-028", "CAP-144", "CAP-174"],
        ["ddos", "cloudflare", "aws-shield", "traffic-scrubbing", "resilience"]
    ),
    (
        "CAP-146", "Secret Scanning & Automated Credential Hygiene",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Detect committed secrets, cloud API keys, and private tokens in source code repositories before merge.",
        ["Leaked AWS or OpenAI keys leading to tens of thousands in unauthorized usage within hours", "Revocation scrambles during security emergencies", "Public exposure of internal database passwords in git history"],
        ["Gitleaks", "TruffleHog", "GitHub Secret Scanning", "GitGuardian", "Semgrep Secrets"],
        ["CAP-014", "CAP-032", "CAP-157", "CAP-170"],
        ["secret-scanning", "gitleaks", "trufflehog", "credential-hygiene", "security"]
    ),
    (
        "CAP-147", "Hardware Security Module (HSM) & Key Custody",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Manage root cryptographic keys, certificate signing, and transaction signing within tamper-resistant hardware.",
        ["Theft of master private keys allowing attackers to forge certificates or decrypt historical logs", "Non-compliance with FIPS 140-2 Level 3 regulatory requirements", "Uncontrolled multi-party access to corporate treasury wallets"],
        ["YubiHSM", "AWS CloudHSM", "HashiCorp Vault Transit", "Google Cloud KMS", "Nitrokey HSM"],
        ["CAP-019", "CAP-032", "CAP-148", "CAP-157"],
        ["hsm", "kms", "key-custody", "fips-140", "cryptography"]
    ),
    (
        "CAP-148", "FIDO2 & Passwordless WebAuthn Authentication",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Replace phishable passwords with hardware-backed public key cryptography and biometric passkeys.",
        ["Credential harvesting phishing attacks tricking employees into surrendering passwords and SMS OTPs", "High user friction and password reset support tickets", "Account takeover risks from leaked third-party password dumps"],
        ["WebAuthn API", "SimpleWebAuthn", "YubiKey", "Apple Passkeys", "Corbado"],
        ["CAP-002", "CAP-141", "CAP-147", "CAP-158"],
        ["fido2", "webauthn", "passkeys", "yubikey", "passwordless"]
    ),
    (
        "CAP-149", "Automated Penetration Testing & Breach Simulation",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Simulate adversary techniques and attack paths across infrastructure to validate defensive posture.",
        ["Blind spots where security controls look good on paper but fail against real-world exploits", "Year-long gaps between annual penetration test reports", "Failure to detect misconfigured IAM permissions across multi-account clouds"],
        ["Atomic Red Team", "Caldera (MITRE)", "BloodHound", "Metasploit", "Prowler"],
        ["CAP-014", "CAP-124", "CAP-152", "CAP-170"],
        ["penetration-testing", "adversary-simulation", "caldera", "bloodhound", "red-team"]
    ),
    (
        "CAP-150", "Intrusion Detection & Prevention Systems (IDS/IPS)",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Monitor network traffic and kernel system calls to detect and block malicious command executions.",
        ["Undetected lateral movement after an initial server compromise", "Execution of reverse shells and cryptocurrency miners on production compute", "Inability to stop active exploitation attempts in real time"],
        ["Falco", "Suricata", "Snort", "Zeek", "Wazuh"],
        ["CAP-009", "CAP-011", "CAP-151", "CAP-153"],
        ["ids", "ips", "falco", "suricata", "threat-detection"]
    ),
    (
        "CAP-151", "Security Information & Event Management (SIEM)",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Aggregate, normalize, and correlate security logs across all endpoints, clouds, and services.",
        ["Security logs scattered across separate cloud consoles with zero centralized visibility", "Failure to reconstruct attacker timelines following an incident", "Missed multi-stage attack patterns that only become visible through correlation"],
        ["Wazuh", "Elastic Security", "Splunk", "Google Chronicle", "OpenSearch Security"],
        ["CAP-011", "CAP-023", "CAP-150", "CAP-152"],
        ["siem", "wazuh", "log-correlation", "security-operations", "soc"]
    ),
    (
        "CAP-152", "Threat Hunting & Threat Intelligence Feeds",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Proactively search internal systems for Advanced Persistent Threats (APTs) using global IOC feeds.",
        ["Attackers dwelling inside corporate infrastructure for an average of 200+ days undetected", "Lack of context regarding whether an observed probe is part of a targeted campaign", "Inability to ingest and act upon government and industry threat intelligence bulletins"],
        ["MISP", "OpenCTI", "YARA", "Sigma Rules", "AlienVault OTX"],
        ["CAP-149", "CAP-150", "CAP-151", "CAP-169"],
        ["threat-hunting", "threat-intelligence", "misp", "opencti", "sigma-rules"]
    ),
    (
        "CAP-153", "Runtime Application Self-Protection (RASP)",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Embed instrumentation inside application runtimes to intercept attacks from the inside out.",
        ["WAF evasion using complex string encoding and obfuscation techniques", "Zero-day vulnerabilities in third-party runtime frameworks", "False positives from external firewalls blocking legitimate user business requests"],
        ["Sqreen (Datadog)", "Contrast Security", "OpenTelemetry Security", "pyrasp", "Signal Sciences"],
        ["CAP-014", "CAP-124", "CAP-144", "CAP-150"],
        ["rasp", "runtime-security", "appsec", "sqreen", "self-protection"]
    ),
    (
        "CAP-154", "Container Hardening & Rootless Execution",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-026-utilities-infrastructure", "Utilities & Infrastructure",
        "Run containers with non-root users, read-only root filesystems, and stripped Linux capabilities.",
        ["Container escape vulnerabilities granting attackers full host node root access", "Malicious modification of system binaries inside running containers", "Inability to pass PCI-DSS or SOC 2 container security audits"],
        ["Docker Rootless", "Distroless Images", "Podman", "AppArmor", "SELinux"],
        ["CAP-009", "CAP-150", "CAP-155", "CAP-158"],
        ["container-hardening", "distroless", "rootless", "podman", "selinux"]
    ),
    (
        "CAP-155", "Container Image Vulnerability Scanning",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-026-utilities-infrastructure", "Utilities & Infrastructure",
        "Scan base container images and OS packages for known CVEs during CI build and registry storage.",
        ["Deploying outdated base images containing high-severity unpatched CVEs", "Silent introduction of compromised libraries via unverified container registries", "Lack of policy gates preventing vulnerable containers from launching in production"],
        ["Trivy", "Clair", "Grype", "Harbor Registry Scanner", "Docker Scout"],
        ["CAP-008", "CAP-009", "CAP-014", "CAP-154"],
        ["container-security", "trivy", "grype", "cve-scanning", "vulnerability-management"]
    ),
    (
        "CAP-156", "Cryptographic Signature Verification & Attestation",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Sign software artifacts, containers, and commits to guarantee origin and code integrity.",
        ["Man-in-the-middle tampering of compiled binaries between CI and production", "Execution of unauthorized or rogue container images in production clusters", "Spoofed git commits masquerading as senior engineering releases"],
        ["Cosign (Sigstore)", "Notary Project", "In-Toto", "GPG Commit Signing", "Rekor"],
        ["CAP-008", "CAP-125", "CAP-147", "CAP-168"],
        ["artifact-signing", "sigstore", "cosign", "supply-chain-security", "in-toto"]
    ),
    (
        "CAP-157", "Public Key Infrastructure (PKI) & Cert Automation",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Issue, renew, and revoke private and public TLS/x509 certificates automatically.",
        ["Outages caused by forgotten TLS certificate expirations bringing down public websites", "Manual labor generating CSRs and installing certificates", "Inability to maintain internal corporate private root Certificate Authorities"],
        ["Let's Encrypt / Certbot", "Cert-Manager", "Smallstep CA", "HashiCorp Vault PKI", "OpenSSL"],
        ["CAP-001", "CAP-022", "CAP-143", "CAP-147"],
        ["pki", "tls", "lets-encrypt", "cert-manager", "x509"]
    ),
    (
        "CAP-158", "Sandboxing & MicroVM Workload Isolation",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-024-technology-software", "Technology & Software",
        "Isolate untrusted user-submitted code and AI execution within hardware-virtualized microVMs.",
        ["Malicious user scripts breaking out to access host CPU, RAM, and network interfaces", "Multi-tenant data leakage when executing tenant code on shared worker nodes", "Server resource starvation from runaway malicious forks"],
        ["Firecracker", "gVisor", "Wasmtime", "Docker Sandbox", "Kata Containers"],
        ["CAP-009", "CAP-021", "CAP-078", "CAP-154"],
        ["sandboxing", "firecracker", "gvisor", "microvms", "isolation"]
    ),
    (
        "CAP-159", "Endpoint Detection & Response (EDR) Fleet Security",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Continuously monitor and protect engineer laptops and production servers against malware and exploits.",
        ["Ransomware spreading across developer workstations following a phishing click", "Unmonitored developer machines leaking source code and SSH credentials", "Delayed incident containment allowing compromised laptops to access cloud consoles"],
        ["Osquery", "Wazuh Agent", "CrowdStrike Falcon", "Velociraptor", "FleetDM"],
        ["CAP-011", "CAP-150", "CAP-151", "CAP-169"],
        ["edr", "osquery", "endpoint-security", "fleetdm", "incident-response"]
    ),
    (
        "CAP-160", "Least-Privilege Role & Privilege Escalation Defense",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Enforce strict temporary privilege elevation with automated expiration and dual-custody approvals.",
        ["Engineers possessing permanent admin privileges across all cloud production accounts", "Accidental destruction of resources by accounts with over-broad wildcards (`*`)", "Attacker lateral movement by compromising over-privileged developer IAM roles"],
        ["AWS IAM Identity Center", "Teleport", "Apolicy", "Sudoers rules", "Step-Up Auth"],
        ["CAP-003", "CAP-141", "CAP-142", "CAP-170"],
        ["least-privilege", "teleport", "iam", "access-governance", "privilege-escalation"]
    ),
    (
        "CAP-161", "Immutable Audit Logging & Tamper Proofing",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-016-legal-compliance", "Legal & Compliance",
        "Ship audit logs to append-only, cryptographically sealed storage resistant to attacker modification.",
        ["Attackers clearing `/var/log` and cloud logs to conceal their intrusion footprint", "Inability to prove compliance with financial audit trail regulations", "Disputed actions where employees claim logs were altered retroactively"],
        ["AWS S3 Object Lock (WORM)", "Sigstore Rekor", "Fluency Logs", "Vector / Logstash", "Qdrant Audit Trails"],
        ["CAP-011", "CAP-015", "CAP-151", "CAP-284"],
        ["audit-logging", "worm-storage", "tamper-proof", "compliance", "append-only"]
    ),
    (
        "CAP-162", "Cloud Security Posture Management (CSPM)",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Continuously audit cloud provider configurations against CIS benchmarks and best practices.",
        ["Accidental creation of public-readable S3 buckets containing sensitive customer data", "Unrestricted security groups opening database ports (`5432`) to the world (`0.0.0.0/0`)", "Cloud account drift away from established security baseline policies"],
        ["Prowler", "ScoutSuite", "Steampipe", "CloudQuery", "Wiz"],
        ["CAP-034", "CAP-149", "CAP-160", "CAP-170"],
        ["cspm", "prowler", "cloud-security", "steampipe", "cis-benchmarks"]
    ),
    (
        "CAP-163", "Privacy-Preserving Computation & Homomorphic Encryption",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Perform computations and analytical aggregations on encrypted data without decrypting it.",
        ["Inability to collaborate on joint datasets with hospital or financial partners due to confidentiality laws", "Third-party cloud providers having visibility into raw decrypted customer records", "Exposure of confidential business logic during third-party outsourcing"],
        ["Microsoft SEAL", "OpenFHE", "PySyft", "Concrete (Zama)", "TFHE"],
        ["CAP-015", "CAP-059", "CAP-164", "CAP-165"],
        ["privacy-preserving", "homomorphic-encryption", "seal", "cryptography", "confidential-computing"]
    ),
    (
        "CAP-164", "Zero-Knowledge Proofs (ZKP) & Verification",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-034-decentralized-web3", "Decentralized & Web3",
        "Verify cryptographic claims and transactions without revealing the underlying private data.",
        ["Need to expose full user income or identity documents just to verify eligibility", "Public blockchain transactions exposing proprietary company financial flows", "Inability to audit enterprise systems without viewing trade secrets"],
        ["Circom / SnarkJS", "Noir (Aztec)", "Halo2", "RiscZero", "ZoKrates"],
        ["CAP-019", "CAP-163", "CAP-165", "CAP-204"],
        ["zero-knowledge", "zkp", "circom", "snark", "privacy"]
    ),
    (
        "CAP-165", "Data Loss Prevention (DLP) & Exfiltration Blocking",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Scan and block unauthorized transfers of sensitive corporate data, code, and customer records.",
        ["Disgruntled employees copying customer databases to personal USB drives or cloud drives", "Pasting sensitive private customer PII into public third-party AI chatbots", "Accidental public emailing of internal financial models and spreadsheets"],
        ["Nightfall AI", "Symantec DLP", "Microsoft Purview", "OpenDLP", "TruffleHog Posture"],
        ["CAP-015", "CAP-058", "CAP-088", "CAP-161"],
        ["dlp", "data-loss-prevention", "exfiltration", "nightfall", "confidentiality"]
    ),
    (
        "CAP-166", "Virtual Private Cloud (VPC) & Network Segmentation",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-026-utilities-infrastructure", "Utilities & Infrastructure",
        "Isolate backend workloads into private subnets with strict security group egress/ingress rules.",
        ["Direct internet routability to production database and cache instances", "Breach of a single staging server exposing production network traffic", "Lack of visibility into cross-service packet flows and network boundaries"],
        ["AWS VPC", "Terraform VPC Modules", "Cilium Network Policies", "Calico CNI", "WireGuard Subnets"],
        ["CAP-009", "CAP-021", "CAP-034", "CAP-142"],
        ["vpc", "network-segmentation", "subnets", "firewalls", "calico"]
    ),
    (
        "CAP-167", "Secure Enclave Execution & Confidential Computing",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Execute mission-critical workloads inside hardware-isolated memory enclaves shielded from the host OS.",
        ["Cloud provider hypervisors having potential memory access to proprietary AI weights or cryptographic keys", "Malicious host administrators inspecting private memory spaces", "Inability to guarantee code integrity in untrusted multi-tenant host environments"],
        ["AWS Nitro Enclaves", "Intel SGX", "AMD SEV", "Gramine", "Anjuna"],
        ["CAP-019", "CAP-084", "CAP-147", "CAP-158"],
        ["confidential-computing", "nitro-enclaves", "intel-sgx", "hardware-isolation", "security"]
    ),
    (
        "CAP-168", "Supply Chain Security Verification (SLSA)",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Attest build provenance from source code to final deployment to prevent supply chain poisoning.",
        ["Compromise of build servers injecting backdoors into legitimate compiled releases (SolarWinds style)", "Inability to prove that a running container matches the exact audited git commit", "Developers pulling typosquatted malicious packages from public registries"],
        ["SLSA Framework", "Sigstore", "TUF (The Update Framework)", "Macaroons", "Chainguard Images"],
        ["CAP-008", "CAP-125", "CAP-156", "CAP-169"],
        ["supply-chain-security", "slsa", "sigstore", "tuf", "provenance"]
    ),
    (
        "CAP-169", "Digital Forensics & Incident Response (DFIR)",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Preserve memory snapshots, analyze disk images, and reconstruct attack kill chains during breaches.",
        ["Contamination of legal evidence by improperly investigating compromised servers", "Inability to determine the exact initial entry vector of an intrusion", "Prolonged dwell time while responders blindly guess attacker movements"],
        ["Velociraptor", "Volatility Framework", "Autopsy", "Plaso (log2timeline)", "GRR Rapid Response"],
        ["CAP-011", "CAP-151", "CAP-159", "CAP-170"],
        ["dfir", "digital-forensics", "incident-response", "velociraptor", "volatility"]
    ),
    (
        "CAP-170", "Threat Modeling & STRIDE Architecture Auditing",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Analyze architectural designs systematically to identify and mitigate threat vectors prior to coding.",
        ["Architectural security flaws that cannot be patched with simple code bug fixes", "Wasted engineering cycles re-architecting systems after failing security audits", "Unclear threat boundaries leading to misplaced security engineering investments"],
        ["OWASP Threat Dragon", "Microsoft Threat Modeling Tool", "STRIDE Methodology", "PyTM", "IriusRisk"],
        ["CAP-001", "CAP-014", "CAP-149", "CAP-294"],
        ["threat-modeling", "stride", "appsec", "owasp", "architecture-security"]
    ),
    (
        "CAP-171", "Automated Compliance Auditing & SOC 2 Continuous Monitoring",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-016-legal-compliance", "Legal & Compliance",
        "Continuously collect configuration evidence and policy attestations to prove compliance automatically.",
        ["Scrambling for weeks before annual audits to manually screenshot cloud consoles", "Lapse of security controls between audit windows leading to undetected vulnerabilities", "High audit fees caused by manual CPA evidence verification"],
        ["Drata", "Vanta", "Steampipe Compliance", "Secureframe", "Sprinto"],
        ["CAP-015", "CAP-161", "CAP-162", "CAP-284"],
        ["compliance-automation", "soc2", "vanta", "drata", "continuous-monitoring"]
    ),
    (
        "CAP-172", "Security Policy as Code (Open Policy Agent)",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Express and enforce corporate security policies across Kubernetes, Terraform, and APIs declaratively.",
        ["Engineers deploying unapproved open security groups or non-compliant containers", "Manual security reviews slowing down delivery pipelines", "Inconsistent policy enforcement across cloud, on-prem, and container stacks"],
        ["Open Policy Agent (OPA)", "Conftest", "Kyverno", "Checkov", "OPA Gatekeeper"],
        ["CAP-003", "CAP-009", "CAP-034", "CAP-171"],
        ["policy-as-code", "opa", "kyverno", "conftest", "governance"]
    ),
    (
        "CAP-173", "Secure Remote Access & Private Mesh Tunnels",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-022-telecommunications-connectivity", "Telecommunications & Connectivity",
        "Connect remote engineer machines and localized servers into an encrypted, identity-aware wireguard mesh.",
        ["Opening SSH ports (`22`) to the public internet exposing servers to brute-force scans", "Fragmented, unreliable corporate VPNs dropping connections during large file transfers", "Lack of centralized multi-factor authentication for server terminal sessions"],
        ["Tailscale", "WireGuard", "Nebula (Slack)", "Netmaker", "Twingate"],
        ["CAP-021", "CAP-142", "CAP-143", "CAP-174"],
        ["mesh-vpn", "tailscale", "wireguard", "remote-access", "encryption"]
    ),
    (
        "CAP-174", "Blast Radius Containment & Network Isolation",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Segment critical production assets into isolated fault domains to restrict attacker damage.",
        ["A compromise in a staging environment escalating into full production database deletion", "Ransomware encrypting all company storage buckets from a single compromised node", "Inability to safely contain a live breach without shutting down the entire enterprise"],
        ["AWS Multi-Account (Organizations)", "Cilium Network Policies", "AWS SCPs", "Microsegmentation", "Canary Blast Radius"],
        ["CAP-009", "CAP-142", "CAP-166", "CAP-170"],
        ["blast-radius", "containment", "microsegmentation", "isolation", "resilience"]
    ),
    (
        "CAP-175", "Ransomware Defense & Immutable Backup Recovery",
        "Tier 5: Cybersecurity & Zero Trust Architecture",
        "SEC-033-cybersecurity-privacy", "Cybersecurity & Privacy",
        "Protect corporate databases and backups against encryption attacks using air-gapped, immutable snapshots.",
        ["Attackers gaining admin access and deleting both live systems and backups simultaneously", "Paying extortion demands to recover encrypted critical company intellectual property", "Inability to restore verified clean system states after malware infection"],
        ["AWS S3 Object Lock", "Bacula", "Veeam Immutable", "ZFS Air-Gapped Snapshots", "Restic"],
        ["CAP-012", "CAP-030", "CAP-161", "CAP-174"],
        ["ransomware-defense", "immutable-backups", "s3-object-lock", "disaster-recovery", "air-gap"]
    ),

    # Tier 6: FinTech, Commerce & Monetization (CAP-176 to CAP-210)
    (
        "CAP-176", "Payment Gateway Integration & Processing",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Integrate credit card, Apple Pay, Google Pay, and localized payment rails via developer APIs.",
        ["Failed checkout conversions due to missing regional payment methods", "High merchant fees from un-optimized payment gateway routing", "Non-compliance with complex credit card network regulations"],
        ["Stripe API", "Adyen", "Braintree / PayPal", "Square", "Checkout.com"],
        ["CAP-001", "CAP-177", "CAP-178", "CAP-187"],
        ["payments", "stripe", "adyen", "credit-cards", "checkout"]
    ),
    (
        "CAP-177", "Idempotent Transaction Processing & Concurrency",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Prevent duplicate billing and race conditions using deterministic idempotency keys and transactional locks.",
        ["Customers getting billed multiple times for a single purchase during network retries", "Inventory sold to multiple buyers simultaneously due to race conditions", "Ledger corruption from unhandled partial network failures"],
        ["Idempotency-Key Header", "PostgreSQL Advisory Locks", "Redis Redlock", "Transactional Outbox Pattern", "Stripe Idempotency"],
        ["CAP-004", "CAP-067", "CAP-176", "CAP-183"],
        ["idempotency", "transaction-processing", "concurrency", "distributed-locking", "billing"]
    ),
    (
        "CAP-178", "Subscription Lifecycle & Recurring Billing",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Manage tiered pricing plans, trial periods, upgrades, downgrades, churn, and automated dunning.",
        ["Revenue loss from failed recurring credit card payments that are never retried", "Customer confusion and billing disputes during prorated mid-cycle plan changes", "High engineering overhead hand-coding subscription state machines"],
        ["Stripe Billing", "Chargebee", "Paddle", "Recurly", "Kill Bill"],
        ["CAP-176", "CAP-177", "CAP-199", "CAP-291"],
        ["subscriptions", "recurring-billing", "stripe-billing", "dunning", "saas-pricing"]
    ),
    (
        "CAP-179", "Multi-Currency Exchange & FX Settlement",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Support dynamic real-time currency conversion, hedging, and localized foreign exchange settlement.",
        ["Shocking customers with surprise international conversion bank fees", "Margin erosion caused by unhedged currency volatility across international ventures", "Complex multi-currency accounting reconciliation overhead"],
        ["Wise API", "Fixer.io", "Open Exchange Rates", "Stripe Multi-Currency", "Currencylayer"],
        ["CAP-020", "CAP-176", "CAP-183", "CAP-205"],
        ["multi-currency", "foreign-exchange", "wise", "fx-settlement", "global-commerce"]
    ),
    (
        "CAP-180", "Payment Fraud Detection & Risk Scoring",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Analyze incoming transactions with machine learning models to detect and block fraudulent card charges.",
        ["Costly chargeback fees and fines from card networks exceeding chargeback thresholds", "False positives turning away high-value legitimate customers", "Account takeover fraud depleting customer stored balances"],
        ["Stripe Radar", "Sift", "SEON", "FingerprintJS", "FraudLabs Pro"],
        ["CAP-016", "CAP-061", "CAP-176", "CAP-188"],
        ["fraud-detection", "stripe-radar", "risk-scoring", "chargebacks", "anti-fraud"]
    ),
    (
        "CAP-181", "Automated Invoicing & Accounts Receivable (AR)",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Generate, dispatch, and track structured electronic invoices with automated payment reminders.",
        ["Cash flow crunches caused by 60+ day overdue customer invoices", "Manual accounting hours spent drafting and emailing PDF invoices", "Mismatched invoice payments creating unallocated cash reserves"],
        ["Stripe Invoicing", "FreshBooks API", "QuickBooks Invoicing", "Bill.com", "Anvil PDF"],
        ["CAP-020", "CAP-178", "CAP-183", "CAP-290"],
        ["invoicing", "accounts-receivable", "billing", "dunning", "automation"]
    ),
    (
        "CAP-182", "Merchant Settlement & Split Payouts",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Route customer payments and split disbursements automatically to multi-party marketplace sellers.",
        ["Manual spreadsheet calculations to disburse weekly vendor earnings", "Legal liabilities holding customer funds without required money transmitter licenses", "Errors in calculating marketplace platform commission cuts"],
        ["Stripe Connect", "Adyen for Platforms", "PayPal Marketplace", "Routable", "Dwolla"],
        ["CAP-176", "CAP-177", "CAP-189", "CAP-205"],
        ["split-payouts", "stripe-connect", "marketplace-payments", "settlement", "escrow"]
    ),
    (
        "CAP-183", "Double-Entry Bookkeeping & Financial Ledgers",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-008-financial-services", "Financial Services",
        "Maintain immutable, balanced debit-and-credit ledgers for all monetary transactions and internal accounts.",
        ["Unbalanced financial books making accurate auditing impossible", "Inability to reconstruct historical account balances at specific points in time", "Financial discrepancies between application balances and external bank statements"],
        ["Ledger CLI", "Beancount", "Modern Treasury Ledgers", "Fragment", "Formance (Numary)"],
        ["CAP-004", "CAP-020", "CAP-177", "CAP-194"],
        ["double-entry", "bookkeeping", "ledger", "beancount", "formance"]
    ),
    (
        "CAP-184", "Automated Financial Auditing & Reconciliation",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-008-financial-services", "Financial Services",
        "Continuously reconcile bank statement line items against internal application transaction logs.",
        ["Accountants spending weeks at quarter-end hunting for missing pennies", "Undetected payment gateway settlement slippage draining corporate margins", "Audit failures due to lack of verifiable reconciliation proof"],
        ["Modern Treasury", "BlackLine", "FloQast", "Plaid Transactions", "Recon Engine"],
        ["CAP-015", "CAP-020", "CAP-183", "CAP-194"],
        ["reconciliation", "financial-audit", "modern-treasury", "plaid", "accounting"]
    ),
    (
        "CAP-185", "Credit Scoring & Underwriting Algorithms",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Evaluate borrower creditworthiness, cash flow health, and default probabilities using automated models.",
        ["High default rates on merchant cash advances or deferred customer loans", "Manual underwriting processes taking days to approve simple business lines of credit", "Algorithmic bias violating fair lending regulations"],
        ["Plaid Assets/Income", "Credit Kudos", "FICO SDK", "XGBoost Credit Scorer", "Nova Credit"],
        ["CAP-016", "CAP-089", "CAP-180", "CAP-206"],
        ["credit-scoring", "underwriting", "fintech", "plaid", "risk-assessment"]
    ),
    (
        "CAP-186", "Global Sales Tax & VAT Calculation Engine",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-008-financial-services", "Financial Services",
        "Calculate real-time sales tax, VAT, and GST rates across jurisdictions and generate filing reports.",
        ["Severe tax penalties and audits from selling across state and international borders without tax collection", "Inability to maintain thousands of changing municipal tax rate rules manually", "Overcharging customers on tax-exempt products harming sales conversions"],
        ["Stripe Tax", "TaxJar", "Avalara AvaTax", "Anrok", "Quaderno"],
        ["CAP-015", "CAP-176", "CAP-181", "CAP-284"],
        ["sales-tax", "vat", "taxjar", "avalara", "stripe-tax"]
    ),
    (
        "CAP-187", "PCI-DSS Scope Reduction & Tokenization",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Handle sensitive credit card numbers exclusively through tokenized iframe fields to bypass PCI scope.",
        ["Massive annual compliance costs and security liabilities of storing raw PAN card numbers", "Severe catastrophic liability in the event of database exfiltration", "Inability to accept card payments legally without Level 1 certification"],
        ["Stripe Elements", "Basis Theory", "VGS (Very Good Security)", "Adyen Drop-in", "TokenEx"],
        ["CAP-002", "CAP-015", "CAP-176", "CAP-180"],
        ["pci-dss", "tokenization", "vgs", "stripe-elements", "card-security"]
    ),
    (
        "CAP-188", "Dispute & Chargeback Defense Management",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Automate the collection of delivery proof and submit evidence to dispute illegitimate chargebacks.",
        ["Revenue loss from fraudulent 'friendly fraud' chargebacks", "Merchant accounts getting terminated by Visa/Mastercard for exceeding 1% dispute rates", "Hours wasted compiling shipping tracking numbers and user logs for bank responses"],
        ["Stripe Chargeback Protection", "Chargeflow", "Midigator", "Disputeifier", "Signifyd"],
        ["CAP-176", "CAP-180", "CAP-181", "CAP-187"],
        ["chargebacks", "dispute-management", "chargeflow", "chargeback-defense", "fraud"]
    ),
    (
        "CAP-189", "Marketplace Escrow & Milestone Hold Engine",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-029-marketplace-platform", "Marketplace & Platform",
        "Hold funds securely in escrow until buyer milestone approvals or physical shipment confirmations.",
        ["Buyer fraud claiming non-delivery while merchant already shipped valuable goods", "Merchant insolvency before fulfilling high-value custom client orders", "Legal issues operating unauthorized holding escrow services"],
        ["Escrow.com API", "Stripe Connect Escrow", "Tazapay", "Mangopay", "Castle"],
        ["CAP-177", "CAP-182", "CAP-183", "CAP-204"],
        ["escrow", "marketplace-escrow", "milestone-payments", "buyer-protection", "fintech"]
    ),
    (
        "CAP-190", "Algorithmic Dynamic Pricing & Yield Optimization",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-021-retail-e-commerce", "Retail & E-commerce",
        "Adjust prices dynamically based on real-time demand, competitor pricing, inventory levels, and churn risk.",
        ["Leaving substantial revenue on the table during periods of peak customer demand", "Accumulating excess perishable or seasonal inventory due to rigid pricing", "Losing price-sensitive customers to agile dynamic-pricing competitors"],
        ["Pricefx", "Competera", "Dynamic Pricing Engine", "Scikit-Optimize", "Gurobi"],
        ["CAP-016", "CAP-178", "CAP-227", "CAP-291"],
        ["dynamic-pricing", "yield-optimization", "revenue-management", "algorithmic-pricing", "fintech"]
    ),
    (
        "CAP-191", "Financial Modeling, Runway & Burn Forecasting",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-008-financial-services", "Financial Services",
        "Simulate corporate cash runways, hiring scenarios, revenue trajectories, and capital requirements.",
        ["Running out of cash unexpectedly due to lack of visibility into forward burn rates", "Poor strategic planning based on static annual budget spreadsheets", "Inability to present credible financial projections to venture capital investors"],
        ["Causal", "Finmark", "Runway.com", "Pry Financials", "Jupyter Financial Stack"],
        ["CAP-020", "CAP-183", "CAP-193", "CAP-276"],
        ["financial-modeling", "burn-rate", "runway-forecasting", "causal", "fp-and-a"]
    ),
    (
        "CAP-192", "Revenue Recognition Engine (ASC 606 / IFRS 15)",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-008-financial-services", "Financial Services",
        "Amortize deferred revenue and recognize earned revenue in compliance with GAAP ASC 606 standards.",
        ["Misleading financial statements prematurely recognizing annual upfront SaaS payments", "Failed audits and restatements when seeking venture capital or IPO", "Complex manual spreadsheet amortization tables prone to broken formulas"],
        ["Leapfin", "Maxio (SaaSoptics)", "Stripe Revenue Recognition", "Zuora RevPro", "Subscript"],
        ["CAP-020", "CAP-178", "CAP-183", "CAP-194"],
        ["revenue-recognition", "asc-606", "deferred-revenue", "gaap", "saas-accounting"]
    ),
    (
        "CAP-193", "Treasury & Corporate Cash Management",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-008-financial-services", "Financial Services",
        "Monitor multi-bank cash positions, automate sweeps, and optimize yield on operational balances.",
        ["Cash sitting in zero-interest accounts losing purchasing power to inflation", "Overdraft fees caused by unmonitored cash draws across subsidiary accounts", "Counterparty risk exposure during regional banking crises"],
        ["Modern Treasury", "Mercury Treasury API", "Brex Cash", "Treasury Prime", "Kyriba"],
        ["CAP-020", "CAP-183", "CAP-191", "CAP-194"],
        ["treasury-management", "cash-flow", "modern-treasury", "yield-optimization", "corporate-finance"]
    ),
    (
        "CAP-194", "Payment Gateway Reconciliation & Settlement Auditing",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Match merchant bank deposits against payment gateway gross, net, fee, and refund line items.",
        ["Unexplained variances between credit card settlements and actual bank deposits", "Undetected billing fee increases from payment processors eating margins", "Difficulty separating revenue from customer sales taxes and processing fees"],
        ["Modern Treasury", "Stripe Balance History API", "Adyen Financial Reports", "ReconBot", "Anaplan"],
        ["CAP-020", "CAP-176", "CAP-183", "CAP-184"],
        ["payment-reconciliation", "settlement-auditing", "gateway-fees", "cash-accounting", "fintech"]
    ),
    (
        "CAP-195", "Embedded Banking & Banking-as-a-Service (BaaS)",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Issue white-label FDIC-insured bank accounts, routing numbers, and payment capabilities inside apps.",
        ["High regulatory and capital hurdles to establishing a licensed de-novo bank", "Customers leaving product ecosystem to conduct banking transactions elsewhere", "Missing out on lucrative interchange fee revenue sharing"],
        ["Unit.co", "Stripe Treasury", "Column", "Swan.io", "Treasury Prime"],
        ["CAP-001", "CAP-176", "CAP-183", "CAP-197"],
        ["baas", "embedded-banking", "unit", "stripe-treasury", "virtual-accounts"]
    ),
    (
        "CAP-196", "Point of Sale (POS) Hardware & Reader Integration",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-021-retail-e-commerce", "Retail & E-commerce",
        "Connect physical card readers, barcode scanners, and receipt printers to web and mobile apps.",
        ["Inability to unify in-person retail sales with online e-commerce inventories", "Clunky manual payment entry on standalone card terminals causing clerk mistakes", "Hardware connectivity drops over Bluetooth and USB losing sales"],
        ["Stripe Terminal", "Square Reader SDK", "Adyen POS", "Zebra Scanner SDK", "ESC/POS printer drivers"],
        ["CAP-108", "CAP-176", "CAP-216", "CAP-221"],
        ["pos", "stripe-terminal", "in-person-payments", "retail-hardware", "omnichannel"]
    ),
    (
        "CAP-197", "Digital Wallet & Contactless Token Integration",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Integrate Apple Pay, Google Wallet, and peer-to-peer tokenized pass engines into mobile apps.",
        ["High checkout abandonment on mobile devices when users must type 16-digit card numbers", "Inability to issue digital loyalty cards, boarding passes, and event tickets", "Security risks associated with storing credit cards on client devices"],
        ["Apple Pay Web / PassKit", "Google Wallet API", "Stripe Apple Pay", "PassNinja", "Contactless SDK"],
        ["CAP-108", "CAP-148", "CAP-176", "CAP-195"],
        ["digital-wallet", "apple-pay", "google-wallet", "passkit", "mobile-checkout"]
    ),
    (
        "CAP-198", "Affiliate, Referral & Commission Tracking",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-019-marketing-advertising", "Marketing & Advertising",
        "Track referral links, coupon attributions, multi-tier partner commissions, and payout schedules.",
        ["Inaccurate referral attribution rewarding fraudulent or self-referred clicks", "High administrative overhead calculating and disbursing monthly affiliate commissions", "Unhappy marketing partners due to lack of real-time conversion dashboards"],
        ["Rewardful", "Tolt", "PartnerStack", "Refersion", "Dub.co"],
        ["CAP-176", "CAP-182", "CAP-291", "CAP-296"],
        ["affiliate-tracking", "referrals", "rewardful", "partnerstack", "commissions"]
    ),
    (
        "CAP-199", "Usage-Based Metering & Consumption Billing",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-028-b2b-enterprise-software", "B2B Enterprise Software",
        "Aggregate, meter, and bill high-frequency API calls, storage gigabytes, and compute seconds.",
        ["Inability to monetize AI products whose costs scale with token and GPU consumption", "Billing disputes caused by opaque, un-auditable usage metrics", "Lag in usage aggregation delaying end-of-month invoice generation"],
        ["Lago (Open Source)", "Stripe Usage-Based Billing", "Togai", "Metronome", "Amberflo"],
        ["CAP-001", "CAP-011", "CAP-178", "CAP-181"],
        ["usage-based-billing", "metering", "lago", "metronome", "token-billing"]
    ),
    (
        "CAP-200", "Capital Allocation & Venture Portfolio Optimization",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-027-venture-capital-investment", "Venture Capital & Investment",
        "Model expected venture returns, Kelly criterion bet sizing, and capital efficiency across startups.",
        ["Pouring capital into failing venture experiments while starving breakout opportunities", "Emotional, undisciplined investment decisions without mathematical grounding", "Lack of portfolio diversification across uncorrelated risk vectors"],
        ["Kelly Criterion Engine", "PyPortfolioOpt", "Markowitz Mean-Variance", "Venture Return Simulator", "Monte Carlo Risk"],
        ["CAP-191", "CAP-201", "CAP-276", "CAP-281"],
        ["capital-allocation", "venture-capital", "portfolio-optimization", "kelly-criterion", "investment"]
    ),
    (
        "CAP-201", "Venture Cap Table & Equity Stake Management",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-027-venture-capital-investment", "Venture Capital & Investment",
        "Model multi-round dilution, stock option pools, SAFE notes, and liquidation waterfall scenarios.",
        ["Founders losing company control due to unanticipated financing round dilution", "Mismatched shareholder records causing disputes during acquisition exits", "Errors calculating option vesting and exercise tax liabilities"],
        ["Carta API", "Pulley", "Ledgy", "CapTable CLI", "OpenCapTable format"],
        ["CAP-020", "CAP-183", "CAP-200", "CAP-280"],
        ["cap-table", "equity-management", "dilution", "carta", "vesting"]
    ),
    (
        "CAP-202", "Secondary Market Liquidity & Private Share Trading",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-027-venture-capital-investment", "Venture Capital & Investment",
        "Facilitate compliant transfers, secondary tender offers, and liquidity programs for private equity.",
        ["Key early employees locked into illiquid paper wealth unable to buy homes or pay taxes", "Uncontrolled private share transfers to hostile third-party buyers", "Complex legal paperwork and transfer approvals delaying secondary transactions"],
        ["Forge Global API", "Carta Liquidity", "EquityZen platform", "Caplight", "AngelList Secondary"],
        ["CAP-200", "CAP-201", "CAP-204", "CAP-280"],
        ["secondary-market", "liquidity", "private-shares", "tender-offers", "equity"]
    ),
    (
        "CAP-203", "Tokenized Asset Management & RWA Protocols",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-034-decentralized-web3", "Decentralized & Web3",
        "Tokenize real-world assets, real estate equity, and receivables into compliant on-chain instruments.",
        ["High legal and administrative friction syndicating ownership in real estate and debt", "Lack of 24/7 global trading liquidity for physical infrastructure assets", "Fragile manual record-keeping for asset dividend distributions"],
        ["Centrifuge", "Ondo Finance", "ERC-3643 (T-REX)", "OpenZeppelin Contracts", "Chainlink Proof of Reserve"],
        ["CAP-019", "CAP-164", "CAP-183", "CAP-204"],
        ["rwa", "asset-tokenization", "real-world-assets", "smart-contracts", "web3"]
    ),
    (
        "CAP-204", "Decentralized Escrow & Trustless Settlement",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-034-decentralized-web3", "Decentralized & Web3",
        "Execute trustless on-chain milestone escrow contracts with multi-sig and oracle resolution.",
        ["Counterparty default risk in cross-border trade without access to international courts", "High banking fees on traditional international letters of credit", "Slow multi-day bank settlement times freezing operational liquidity"],
        ["Safe (Gnosis)", "Chainlink Functions", "Aragon Court", "OpenZeppelin Escrow", "Smart Contract Multimig"],
        ["CAP-019", "CAP-164", "CAP-189", "CAP-203"],
        ["decentralized-escrow", "safe-multisig", "oracles", "chainlink", "web3"]
    ),
    (
        "CAP-205", "Cross-Border Remittance & Stablecoin Rails",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Settle international payments in seconds using fiat-backed stablecoins and local off-ramps.",
        ["Losing 3-5% in banking wire fees and foreign exchange markups on overseas payroll", "International payments getting held in correspondent banking queues for days", "Difficulties paying remote international contractors in volatile local currencies"],
        ["USDC (Circle API)", "Stripe Crypto Payouts", "Tether (USDT)", "Bridge.xyz", "Conduit"],
        ["CAP-019", "CAP-176", "CAP-179", "CAP-207"],
        ["cross-border", "stablecoins", "usdc", "remittance", "crypto-payouts"]
    ),
    (
        "CAP-206", "Automated Insurance Underwriting & Claims Engine",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-015-insurance", "Insurance",
        "Ingest telemetry, score risk parameters, and automate instant claim adjudication and payouts.",
        ["Slow, paper-heavy insurance claims processing taking weeks to pay out policyholders", "High loss ratios from inaccurate manual actuarial risk pricing", "Fraudulent claims slipping through human manual review"],
        ["Snapsheet API", "Shift Technology", "Guidewire API", "XGBoost Actuarial Engine", "Root Insurance SDK"],
        ["CAP-016", "CAP-180", "CAP-185", "CAP-260"],
        ["insurtech", "underwriting", "claims-automation", "actuarial", "risk"]
    ),
    (
        "CAP-207", "Corporate Expense Cards & Programmable Spend",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Issue virtual corporate cards with programmatic budget limits, MCC restrictions, and receipt matching.",
        ["Employees overspending on unauthorized corporate subscriptions and expenses", "Tedious end-of-month employee expense report reimbursement cycles", "Lack of real-time visibility into distributed company spending"],
        ["Stripe Issuing", "Brex API", "Ramp API", "Lithic", "Marqeta"],
        ["CAP-176", "CAP-181", "CAP-193", "CAP-195"],
        ["corporate-cards", "spend-management", "stripe-issuing", "marqeta", "expense-control"]
    ),
    (
        "CAP-208", "Financial Health & Valuation Benchmarking Dashboards",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-008-financial-services", "Financial Services",
        "Aggregate SaaS metrics (ARR, NRR, CAC Payback, LTV, Rule of 40) into real-time executive views.",
        ["Founders flying blind without real-time visibility into customer acquisition economics", "Conflicting calculations of Monthly Recurring Revenue (MRR) across internal tools", "Difficulty benchmarking performance against top-quartile industry peers"],
        ["Baremetrics", "ChartMogul", "ProfitWell", "Stripe Sigma", "Metabase Financials"],
        ["CAP-020", "CAP-178", "CAP-191", "CAP-298"],
        ["saas-metrics", "mrr", "chartmogul", "financial-health", "benchmarking"]
    ),
    (
        "CAP-209", "Automated Payroll & Global Contractor Compliance",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-014-human-resources-staffing", "Human Resources & Staffing",
        "Automate domestic payroll tax filings and compliant international contractor disbursements.",
        ["Severe tax penalties for misclassifying employees as independent contractors", "Late payroll runs violating local labor laws and destroying team trust", "Complex, manual tax withholdings across multiple international jurisdictions"],
        ["Gusto API", "Deel API", "Rippling API", "Remote.com", "Oyster HR"],
        ["CAP-020", "CAP-182", "CAP-205", "CAP-268"],
        ["payroll", "deel", "gusto", "contractor-compliance", "global-hr"]
    ),
    (
        "CAP-210", "Invoice Factoring & Accounts Receivable Financing",
        "Tier 6: FinTech, Commerce & Monetization",
        "SEC-030-fintech-payments", "Fintech & Payments",
        "Advance capital against outstanding verified customer invoices via automated underwriting.",
        ["Rapidly growing ventures starved of cash while waiting for 90-day enterprise customer payments", "Missing supplier bulk discounts due to trapped accounts receivable", "Predatory high-interest traditional merchant cash advance loans"],
        ["Pipe.com API", "Koxa", "Fundbox", "Lendio API", "Modern Treasury Advances"],
        ["CAP-181", "CAP-183", "CAP-185", "CAP-193"],
        ["invoice-factoring", "working-capital", "pipe", "ar-financing", "fintech"]
    ),
]
