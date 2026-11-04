"""Unit tests for foundational agent classes."""
import unittest
from src.agents.base import BaseAgent, AgentState

class TestBaseAgent(unittest.TestCase):
    def test_agent_initialization(self):
        agent = BaseAgent(name="Sentinel")
        self.assertEqual(agent.state.name, "Sentinel")
        self.assertEqual(agent.state.status, "idle")

    def test_agent_execution(self):
        agent = BaseAgent(name="Sentinel")
        result = agent.run("verify safety bounds")
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["agent"], "Sentinel")
        self.assertIn("verify safety bounds", result["response"])

if __name__ == "__main__":
    unittest.main()

