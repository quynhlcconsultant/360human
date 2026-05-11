# Document Naming Convention

## Format
```
{PREFIX}-{SEQ}_{descriptive-name}.md
```

## Prefix Registry

| Prefix | Domain | Folder | Owner |
|--------|--------|--------|-------|
| `CEO` | CEO directives & vision | 0. CEO - Winston | Winston |
| `PRD` | Product requirements & specs | 1. Product Strategy | Product |
| `MKT` | Market research & insights | 2. Market Research | Marketing |
| `ARCH` | Architecture & technical design | 3. Architecture | Engineering |
| `FE` | Frontend design & UI specs | 4. Frontend Team | Frontend |
| `CRE` | Branding & creative assets | 5. Creative Team | Creative |
| `RTM` | Go-to-market strategy | 6. RTM Strategy | Marketing |
| `API` | API specifications | 3. Architecture | Backend |
| `DB` | Database schemas & migrations | 3. Architecture | Backend |
| `TEST` | Test plans & QA specs | (any) | QA |
| `OPS` | DevOps & deployment | (any) | DevOps |

## Sequence Numbers
- `001-099`: Core/foundational documents
- `100-199`: Detailed specifications
- `200-299`: Implementation guides
- `300-399`: Review & audit docs
- `900-999`: Deprecated/superseded docs

## Examples
```
CEO-001_business-requirements.md      → CEO's core business requirements
PRD-001_product-requirements.md       → Main PRD document
ARCH-001_project-blueprint.md         → Master architecture blueprint
ARCH-002_technical-solutions.md       → Technical solution design
ARCH-100_api-endpoint-specs.md        → Detailed API endpoint specs
FE-001_ui-reference.md                → UI design reference
FE-100_component-library.md           → Component specifications
MKT-001_market-insights.md            → Market research findings
MKT-100_competitor-deep-dive.md       → Detailed competitor analysis
TEST-001_test-strategy.md             → Overall test strategy
OPS-001_deployment-runbook.md         → Deployment procedures
```

## Version Tracking
Documents evolve in-place (edit the .md file directly).
For major revisions, archive the previous version first:
```bash
cp document.md .archive/{description}_v{N}_{date}/
```
