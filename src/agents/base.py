"""Base class for autonomous agent instances."""
from typing import Any, Dict

try:
    from pydantic import BaseModel, Field
except ImportError:
    # Lightweight fallback when running tests in clean environment before pip install
    from dataclasses import dataclass, field

    def Field(default=None, default_factory=None):
        if default_factory is not None:
            return field(default_factory=default_factory)
        return field(default=default)

    class BaseModel:  # type: ignore
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

class AgentState(BaseModel):
    name: str
    status: str = Field(default="idle")
    metadata: Dict[str, Any] = Field(default_factory=dict)

class BaseAgent:
    """Foundational agent interface with structured state."""

    def __init__(self, name: str):
        self.state = AgentState(name=name, status="idle", metadata={})

    def run(self, prompt: str) -> Dict[str, Any]:
        """Execute agent workflow."""
        return {
            "agent": self.state.name,
            "status": "completed",
            "prompt": prompt,
            "response": f"Processed: {prompt}"
        }
