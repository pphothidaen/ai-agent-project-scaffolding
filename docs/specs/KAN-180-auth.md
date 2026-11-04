# Specification: KAN-180 Authentication & Identity Verification

## Overview
Defines authentication protocol and access tokens for autonomous agent interactions within the harness.

## Requirements
- Stateless bearer token validation.
- Agent scope checking based on risk tiering defined in `AGENTS.md`.
- Rejection of requests with insufficient scopes.

