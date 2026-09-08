---
name: official-terraform-iac
description: Official Terraform and OpenTofu infrastructure-as-code (IaC) skill covering declarative HCL, remote state locking, modular cloud provisioning, zero-trust network policies, and CI/CD validation.
source: VoltAgent/awesome-agent-skills
origin: HashiCorp Official Developer Standards
---

[[15-SKILLS/README|15-SKILLS]] | [[16-AGENTS/README|16-AGENTS]] | [[STARTHERE]]

# 🏗️ Official Terraform & IaC Skill

> Authoritative infrastructure-as-code patterns based on HashiCorp Terraform and OpenTofu, remote state locking, and modular cloud architecture.

## 🧠 Core Principles

1. **Immutable Infrastructure**: Changes are applied by replacing or updating declared resources, never through ad-hoc manual console mutations.
2. **State Locking**: Remote backend with state locking (S3 + DynamoDB or Terraform Cloud) is mandatory to prevent concurrent state corruption.
3. **Plan Before Apply**: Always run `terraform plan -out=tfplan` and inspect proposed diffs before executing `terraform apply tfplan`.
4. **Least Privilege Credentials**: IAM roles executing Terraform should hold narrowly scoped permissions for defined resource classes.

---

## 🛠️ Implementation Patterns

### 1. Robust Remote Backend & Provider Config

```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "worldwidebro-tfstate-canonical"
    key            = "infrastructure/production/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "worldwidebro-tflocks"
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "Terraform"
      Company     = "WorldwideBro"
    }
  }
}
```

---

## 🔒 Verification & Compliance Checklist

- [ ] All sensitive variables (`tfvars`) are masked and injected via CI/CD secrets.
- [ ] Drift detection is scheduled via continuous read-only `terraform plan` checks.
- [ ] Destroy actions are protected using `lifecycle { prevent_destroy = true }` on production databases.
