# Card Component

Standard styling for card components.

## Standard

| Property | Value |
|---|---|
| Background | `var(--card-bg)` — `#2E2D32` (dark) / `#FFFFFF` (light) |
| Border | `1px solid var(--border)`, `border-radius: 12px` (lg) |
| Display | `flex`, `flex-direction: column` |
| Hover | `box-shadow` + `border-color: var(--primary)` |

### Header

- Background: `var(--card-header-bg)`
- Content: colored icon + title

### Body

- Text color: `var(--text)` with `opacity: 0.85`
- Flex: `flex: 1` (fills remaining card height)
