# .archive - Document Version History

This folder stores original/non-final versions of project documents for rollback purposes.

## Structure
```
.archive/
  {description}_v{version}_{date}/
    {original-folder-structure}/
      {original-files}
```

## Current Archives

### docx-originals_v1.0_2026-03-15
Original .docx files before conversion to .md format.
All 8 documents preserved with original folder structure.

| Original File | Converted To | Notes |
|--------------|-------------|-------|
| Business Requirement_.docx | CEO-001_business-requirements.md | Full text content |
| Checklist.docx | CEO-002_project-checklist.md | Empty (was image-only) |
| PRD.docx | PRD-001_product-requirements.md | Full text content |
| Market Insights.docx | MKT-001_market-insights.md | Text extracted |
| project-blueprint.md.docx | ARCH-001_project-blueprint.md | Full content (2728 words) |
| Technical Solutions.docx | ARCH-002_technical-solutions.md | Full content (1874 words) |
| UI Reference.docx | FE-001_ui-reference.md | Mostly image-based, minimal text |
| UI Writing.docx | FE-002_ui-writing.md | Short UX copy guidelines |

## Rollback Instructions
To restore originals:
```bash
cp -r .archive/docx-originals_v1.0_2026-03-15/* ../
```

## Naming Convention
- `v1.0` = initial version before any edits
- `v1.1, v1.2...` = incremental changes
- `v2.0` = major revision
- Date format: `YYYY-MM-DD`
