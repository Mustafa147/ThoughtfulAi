Thoughtful.ai Package Sorter:

A Python function used to sort packages in Thoughtful.ai's robotic automation factory based on size and weight criteria.

## Objective:
The goal is to automate the classification of packages using a robotic arm. Each package is evaluated by ts **volume** and **mass**, and dispatched to the appropriate stack accordingly.

## Rules:
### Package Identification:
- A package is **Bulky** if:
  - If Volume is **≥ 1,000,000 cm³**, OR
  - Any of its dimensions is **≥ 150 cm**
- A package is **Heavy** if:
  - ITS mass is **≥ 20 kg**

### Stacks:
| Condition                       | Stack    |
|---------------------------------|----------|
| Both **Bulky** and **Heavy**    | REJECTED |
| Either **Bulky** or **Heavy**   | SPECIAL  |
| Neither **Bulky** nor **Heavy** | STANDARD |

## Implementation

The sorting is implemented in the function:
```python
def sort(width, height, length, mass):
    # Returns: "STANDARD", "SPECIAL", or "REJECTED"