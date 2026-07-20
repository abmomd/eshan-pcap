# 📦 Solution: Smart Store Utility Toolkit

```python
# Import entire billing module
import billing

# Import specific function
from discount import apply_discount

# Import module using alias
import inventory as inv

# Import function using alias
from reports import daily_report as report

print("=== QuickMart Billing System ===\n")

# Check stock
inv.check_stock()

# Apply discount
apply_discount()

# Generate bill
billing.generate_bill()

# Calculate tax
billing.calculate_tax()

# Update inventory
inv.update_stock()

# Generate report
report()
```

---

## Output (Example)

```text
=== QuickMart Billing System ===

Checking Stock...

Discount Applied...

Generating Bill...

Calculating Tax...

Updating Inventory...

Generating Daily Report...
```

---

# Concepts Used

## Import Entire Module

```python
import billing
```

Functions are accessed using:

```python
billing.generate_bill()
billing.calculate_tax()
```

---

## Import Specific Function

```python
from discount import apply_discount
```

Used directly as:

```python
apply_discount()
```

---

## Module Alias

```python
import inventory as inv
```

Used as:

```python
inv.check_stock()
```

---

## Function Alias

```python
from reports import daily_report as report
```

Used as:

```python
report()
```

---

# Skills Practiced

- Organizing code into multiple modules
- Using dot notation
- Importing specific functions
- Creating aliases with `as`
- Combining multiple modules in one application