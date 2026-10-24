import csv
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

BASE = Path(__file__).resolve().parent
INPUT_FILE = BASE / "sales_data.csv"
REPORT_FILE = BASE / "sales_report.txt"
SUMMARY_FILE = BASE / "product_summary.csv"

CENT = Decimal("0.01")


def money(value: Decimal) -> str:
    return f"${value.quantize(CENT, rounding=ROUND_HALF_UP):,.2f}"


def analyze(path: Path):
    total_revenue = Decimal("0")
    revenue_by_product = defaultdict(Decimal)
    quantity_by_product = defaultdict(int)
    revenue_by_day = defaultdict(Decimal)

    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            quantity = int(row["quantity"])
            price = Decimal(row["price"])  # Decimal avoids float rounding errors
            revenue = quantity * price

            total_revenue += revenue
            revenue_by_product[row["product"]] += revenue
            quantity_by_product[row["product"]] += quantity
            revenue_by_day[row["date"]] += revenue

    best_day = max(revenue_by_day, key=revenue_by_day.get) if revenue_by_day else None
    return total_revenue, revenue_by_product, quantity_by_product, revenue_by_day, best_day


def write_report(total, rev_prod, qty_prod, rev_day, best_day):
    lines = [
        "=" * 44,
        "SALES REPORT".center(44),
        "=" * 44,
        f"Total revenue: {money(total)}",
        "",
        "Revenue and quantity by product",
        "-" * 44,
        f"{'Product':<14}{'Quantity':>10}{'Revenue':>20}",
    ]
    for product in sorted(rev_prod):
        lines.append(f"{product:<14}{qty_prod[product]:>10}{money(rev_prod[product]):>20}")
    lines += ["", "Revenue by day", "-" * 44]
    for day in sorted(rev_day):
        lines.append(f"{day:<14}{money(rev_day[day]):>30}")
    lines += [
        "",
        f"Highest revenue day: {best_day} ({money(rev_day[best_day])})" if best_day else "No data.",
        "=" * 44,
    ]
    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_summary(rev_prod, qty_prod):
    with open(SUMMARY_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["product", "total_quantity", "total_revenue"])
        for product in sorted(rev_prod):
            writer.writerow([product, qty_prod[product], f"{rev_prod[product].quantize(CENT)}"])


def main():
    total, rev_prod, qty_prod, rev_day, best_day = analyze(INPUT_FILE)
    write_report(total, rev_prod, qty_prod, rev_day, best_day)
    write_summary(rev_prod, qty_prod)
    print(REPORT_FILE.read_text(encoding="utf-8"))
    print(f"Wrote {REPORT_FILE.name} and {SUMMARY_FILE.name}")


if __name__ == "__main__":
    main()