# Logger System Design – Strategy and Factory Patterns

## Overview

This logger system supports multiple output formats: console, file, and (mocked) database. It is implemented using two key design patterns:

- **Strategy Pattern** – Encapsulates different logging behaviors and allows them to be interchanged.
- **Factory Pattern** – Dynamically selects and instantiates the appropriate logger strategy based on configuration or input.

## Design Patterns Used

### Strategy Pattern

- Each logging method (ConsoleLogger, FileLogger, DatabaseLogger) implements the `LoggerStrategy` interface.
- The `Logger` class accepts any strategy and delegates logging to the strategy instance.
- This enables flexible runtime switching of output behavior without altering core logic.

### Factory Pattern

- A `logger_factory(destination: str)` function creates logger strategy instances based on user input or config.
- This centralizes creation logic and simplifies client usage.

## SOLID Principles

- **Single Responsibility**: Each class has a clear, single responsibility (e.g., output logic, delegation, or creation).
- **Open/Closed**: New output formats can be added by creating a new strategy without modifying existing code.
- **Liskov Substitution**: All strategies conform to the `LoggerStrategy` interface and can be used interchangeably.
- **Interface Segregation**: Clients only depend on the abstract `LoggerStrategy` interface, not on unused methods.
- **Dependency Inversion**: `Logger` depends on an abstraction (`LoggerStrategy`), not concrete implementations.

## Trade-offs and Alternatives

### Trade-offs

- **Pros**: Easy to extend and test; output format can be changed at runtime.
- **Cons**: Slightly more complex than using conditional logic inside a single logger class.

### Alternatives

- Without Strategy: Use `if-else` blocks in a monolithic logger class. Less flexible and violates Open/Closed Principle.
- Without Factory: Require the client to instantiate each logger directly, reducing modularity.

## Extensibility

- To add a new output format (e.g., cloud storage), simply:
  1. Create a new class implementing `LoggerStrategy`.
  2. Add a new case in the `logger_factory`.

No changes are required to the `Logger` context or other strategies.

## Example Usage

```python
strategy = logger_factory('file')
logger = Logger(strategy)
logger.log("File logging example.")
