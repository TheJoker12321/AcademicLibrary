from classes.libraries import library


class SystemAdmin:
    total_transactions = 0
    @classmethod
    def update_transactions_count(cls, amount: int = 1) -> None:
        SystemAdmin.total_transactions += 1
    @classmethod
    def report_stats(cls) -> None:
        print("total_transactions:", SystemAdmin.total_transactions)
        print("max days: ", library.Library.max_day_for_lend)