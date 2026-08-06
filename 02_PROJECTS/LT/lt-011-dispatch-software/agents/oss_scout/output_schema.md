# Output schema for OSS Scout Agent

```json
{
  "type": "object",
  "properties": {
    "selected_repo_name": {
      "type": ["string", "null"],
      "description": "The full name of the chosen GitHub repository (owner/repo) or null."
    },
    "suitability_score": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "license_type": {
      "type": "string",
      "description": "MIT, Apache-2.0, BSD, etc."
    },
    "docker_available": {
      "type": "boolean"
    },
    "integration_path": {
      "type": "string",
      "description": "How agents communicate with it: REST, gRPC, or MCP."
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "selected_repo_name",
    "suitability_score",
    "license_type",
    "docker_available",
    "integration_path",
    "reasoning"
  ]
}
```
