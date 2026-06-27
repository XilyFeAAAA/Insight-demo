from src.mcp.errors import InsightMcpError


def test_insight_mcp_error_string_representation() -> None:
    err = InsightMcpError(code="E_TEST", message="boom", details={"k": "v"})

    assert str(err) == "E_TEST: boom"
    assert err.details == {"k": "v"}
