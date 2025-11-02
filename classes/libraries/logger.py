class Logger:
    @staticmethod
    def log_action(action_type: str, details: str) -> None:
        print(f"status book:: {action_type} to {details}")