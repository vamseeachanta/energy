# Energy - Energy Sector Analysis Platform

## Agent OS Documentation

### Product Context
- **Mission & Vision:** @.agent-os/product/mission.md

### Development Standards
- **Code Style:** @.agent-os/standards/code-style.md
- **Best Practices:** @.agent-os/standards/best-practices.md

### Project Management
- **Active Specs:** @.agent-os/specs/
- **Spec Planning:** Use `@.agent-os/instructions/create-spec.md`
- **Tasks Execution:** Use `@.agent-os/instructions/execute-tasks.md`

## Domain Context

Energy is a comprehensive energy sector analysis and project management platform designed for energy industry professionals, researchers, and consultants. The platform specializes in energy market analysis, project tracking, and regulatory compliance management with focus on strategic energy planning and industry intelligence.

## Key Features

- Energy data management and comprehensive market analysis
- Energy project tracking with regulatory compliance management
- Market intelligence and forecasting capabilities
- Technology assessment and policy impact analysis
- Stakeholder management and project coordination
- Technical documentation and compliance tracking

## Workflow Instructions

When asked to work on this codebase:

1. **First**, understand the energy industry context and regulatory environment
2. **Then**, follow the appropriate instruction file:
   - For new features: @.agent-os/instructions/create-spec.md
   - For tasks execution: @.agent-os/instructions/execute-tasks.md
3. **Always**, consider regulatory compliance and industry standards

## Enhanced Features Available

This project supports enhanced Agent OS workflows including:
- **Enhanced Spec Creation**: Prompt summaries, executive summaries, mermaid diagrams, module organization
- **Cross-Repository Integration**: Shared components from AssetUtilities hub (@assetutilities: references)
- **Enhanced Task Execution**: Task summaries, performance tracking, real-time documentation
- **Template Variants**: minimal, standard, enhanced, api_focused, research
- **Visual Documentation**: Auto-generated system architecture and workflow diagrams

### Command Examples
```bash
# Enhanced spec creation
/create-spec feature-name module-name enhanced

# Traditional spec creation (backward compatible)  
/create-spec feature-name

# Enhanced task execution with summaries
/execute-tasks @specs/modules/module-name/spec-folder/tasks.md
```

### Cross-Repository References
- Shared components: @assetutilities:src/modules/agent-os/enhanced-create-specs/
- Sub-agent registry: @assetutilities:agents/registry/sub-agents/workflow-automation
- Hub configuration: @assetutilities:hub-config.yaml


## Important Notes

- **Energy Industry Focus**: All features should be designed with energy sector requirements in mind
- **Regulatory Compliance**: Ensure features support energy industry regulatory and compliance needs
- **Market Analysis**: Prioritize comprehensive energy market analysis and forecasting capabilities
- **Strategic Planning**: Design features that support long-term energy planning and strategic decision making
- **Data Integration**: Support integration of multiple energy data sources and industry databases
- **Technical Standards**: Follow energy industry technical standards and best practices
- Always adhere to established patterns, code style, and best practices documented above

## Available Commands

- **Create-Module-Agent:** Available via `/create-module-agent` command


## Self-Contained Agent OS

This repository includes a complete, self-contained Agent OS framework. All slash commands work immediately after `git clone` with no additional setup required.

### Available Slash Commands
- `/create-spec <spec-name>` - Create detailed specification documents
- `/execute-tasks <tasks-file>` - Execute tasks from specification
- `/create-module-agent <agent-name>` - Create specialized AI agents

### Local Agent OS Structure
- **Standards**: @.agent-os/standards/ (code style, best practices)
- **Instructions**: @.agent-os/instructions/ (workflow guidance)
- **Product Context**: @.agent-os/product/ (mission, roadmap, decisions)
- **Specifications**: @.agent-os/specs/ (feature specifications and tasks)

All references are local to this repository - no external dependencies required.
