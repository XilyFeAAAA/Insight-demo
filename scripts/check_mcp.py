#!/usr/bin/env python3
"""Local smoke check for Insight MCP integration."""

from __future__ import annotations

import asyncio
import json

from src.mcp.insight_adapter import resolve_insight_path
from src.mcp.server import hz_get_metrics
from src.mcp.service import InsightPipelineService


async def _main() -> None:
    insight_path = resolve_insight_path()
    service = InsightPipelineService()
    validation = await service.validate_config(
        insight_path=str(insight_path),
        check_env=False,
    )
    metrics = hz_get_metrics()

    payload = {
        "ok": True,
        "insight_path": str(insight_path),
        "config_path": validation["config_path"],
        "enabled_sources": validation["enabled_sources"],
        "languages": validation["ai"]["languages"],
        "metrics_ok": metrics["ok"],
        "metrics_tool": metrics["tool"],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(_main())
