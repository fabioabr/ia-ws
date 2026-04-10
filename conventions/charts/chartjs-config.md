# Chart.js Configuration

Standard configuration for Chart.js charts.

## Standard

### Library

- Chart.js **v4.4.7** (CDN)
- Colors: `--chart-1` through `--chart-5`, read via `getComputedStyle()`
- Rebuild charts on theme toggle

### Tooltip

| Property | Value |
|---|---|
| Background | `var(--card-bg)` |
| Border | `var(--border)` |
| Border radius | `8px` |

### Grid & Ticks

| Property | Value |
|---|---|
| Grid color | `var(--border)` |
| Tick color | `var(--text-muted)` |
| Tick font | Poppins, `11px` |

### Legend

- `usePointStyle: true`
- `pointStyle: 'circle'`

### Chart Types

| Type | Key Settings |
|---|---|
| Bar | `borderRadius: 6`, `borderSkipped: false` |
| Doughnut | `cutout: '55%'`, height `180px`, legend position `right` |
| Line | `fill: true`, `tension: 0.4`, area opacity `22` |
| Radar | Grid `var(--border)`, `backdropColor: 'transparent'` |
