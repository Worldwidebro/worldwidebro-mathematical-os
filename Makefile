.PHONY: help bootstrap up down restart logs status health seed clean dev test lint format db-shell db-migrate db-backup agents-list agents-start agents-stop ps version prune env-check docker-check neo4j-shell neo4j-init h l u d r b

# ═══════════════════════════════════════════════════════════════════════
# AI BOSS OS - Makefile
# One-command operations for infrastructure, bootstrap, and operations
# ═══════════════════════════════════════════════════════════════════════

bootstrap: ## First-time setup (creates .env, pulls images, starts services)
	@./scripts/bootstrap.sh

up: ## Start all services
	@docker compose up -d
	@echo "✅ Services starting... wait 10s for startup"

down: ## Stop all services
	@docker compose down

restart: ## Restart all services
	@docker compose restart

logs: ## Tail logs (usage: make logs service=postgres)
	@if [ -z "$(service)" ]; then docker compose logs -f; else docker compose logs -f $(service); fi

status: ## Show service status
	@docker compose ps

health: ## Run health checks
	@./scripts/health-check.sh

seed: ## Seed initial data
	@./scripts/seed.sh

clean: ## Remove everything (DESTRUCTIVE)
	@echo "⚠️  This will DELETE all containers and volumes!"; read -p "Type 'yes' to confirm: " confirm && [ "$$confirm" = "yes" ] || (echo "Cancelled"; exit 1); docker compose down -v --remove-orphans

db-shell: ## PostgreSQL shell
	@docker compose exec postgres psql -U postgres -d twenty

db-backup: ## Backup database
	@mkdir -p backups; docker compose exec postgres pg_dump -U postgres twenty > backups/aiboss-$$(date +%Y%m%d-%H%M%S).sql; echo "✅ Backed up"

neo4j-shell: ## Neo4j Cypher shell
	@docker compose exec neo4j cypher-shell -u neo4j -p ventures2026

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "%-20s %s\n", $$1, $$2}'

# Aliases
h: help
u: up
d: down
r: restart
b: bootstrap
s: status
l: logs

.DEFAULT_GOAL := help
