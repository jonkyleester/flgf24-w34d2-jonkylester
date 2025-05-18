from abc import ABC, abstractmethod
import datetime

# --- Strategy Interface ---
class LoggerStrategy(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass

# --- Concrete Strategies ---
class ConsoleLogger(LoggerStrategy):
    def log(self, message: str) -> None:
        print(f"[Console] {datetime.datetime.now()}: {message}")

class FileLogger(LoggerStrategy):
    def __init__(self, filename='log.txt'):
        self.filename = filename

    def log(self, message: str) -> None:
        with open(self.filename, 'a') as file:
            file.write(f"[File] {datetime.datetime.now()}: {message}\n")

class DatabaseLogger(LoggerStrategy):
    def log(self, message: str) -> None:
        # Mock database logging
        print(f"[Database] (Logged to DB): {message}")

# --- Logger Context ---
class Logger:
    def __init__(self, strategy: LoggerStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: LoggerStrategy) -> None:
        self._strategy = strategy

    def log(self, message: str) -> None:
        self._strategy.log(message)

# --- Factory ---
def logger_factory(destination: str) -> LoggerStrategy:
    if destination == 'console':
        return ConsoleLogger()
    elif destination == 'file':
        return FileLogger()
    elif destination == 'database':
        return DatabaseLogger()
    else:
        raise ValueError("Unsupported logger destination")

# --- Example Usage ---
if __name__ == '__main__':
    # Choose a strategy dynamically
    strategy = logger_factory('console')
    logger = Logger(strategy)

    logger.log("System initialized.")

    logger.set_strategy(logger_factory('file'))
    logger.log("File log entry.")

    logger.set_strategy(logger_factory('database'))
    logger.log("Database log entry.")
