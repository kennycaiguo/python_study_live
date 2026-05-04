![img](https://miro.medium.com/v2/resize:fit:875/1*K3LEPC2lc8WNu4HQd_E_EA.png)

## 1. Understanding YAML Syntax

YAML uses indentation and relies on colons (`:`) to define key-value pairs. Unlike JSON, it does not use braces `{}` or brackets `[]` but instead depends on spacing.

## Basic YAML Key-Value Pairs

```
name: John Doe
age: 30
city: New York
```

This structure is equivalent to:

```
{
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}
```

## Correct vs. Incorrect Indentation

### ✅ Correct:

```
person:
  name: Alice
  age: 28
  address:
    city: Los Angeles
    country: USA
```

### ❌ Incorrect:

```
person:
 name: Alice  # Incorrect: Indentation should be 2 spaces
  age: 28
 address:
   city: Los Angeles  # Incorrect: Inconsistent indentation
   country: USA
```

**Fix:** Ensure consistent spacing (usually 2 spaces per level).

## 2. Lists in YAML

Lists in YAML are represented using `-` (hyphens).

## List of Items

```
fruits:
  - Apple
  - Banana
  - Mango
```

Equivalent JSON:

```
{
  "fruits": ["Apple", "Banana", "Mango"]
}
```

## List of Dictionaries

```
employees:
  - name: John
    age: 35
    role: Developer
  - name: Sarah
    age: 29
    role: Designer
```

## Correct vs. Incorrect List Indentation

### ✅ Correct:

```
shopping_list:
  - Milk
  - Bread
  - Eggs
```

### ❌ Incorrect:

```
shopping_list:
- Milk  # Incorrect: No indentation before '-'
 - Bread
 - Eggs
```

**Fix:** Ensure consistent indentation for lists.

## 3. Dictionary (Map) in YAML

A dictionary (also called a map) stores key-value pairs.

## Example of a Dictionary

```
database:
  host: localhost
  port: 5432
  username: admin
  password: secret
```

Equivalent JSON:

```
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "username": "admin",
    "password": "secret"
  }
}
```

## 4. Dictionary Inside a Dictionary

```
company:
  name: TechCorp
  location:
    city: San Francisco
    country: USA
  departments:
    engineering:
      head: Alice
    marketing:
      head: Bob
```

## 5. Dictionary Inside a List

```
servers:
  - name: Server1
    ip: 192.168.1.1
  - name: Server2
    ip: 192.168.1.2
```

## 6. Multi-Line Strings in YAML

There are two ways to write multi-line strings in YAML: `|` (literal block) and `>` (folded block).

## Literal Block (`|`) – Preserves Line Breaks

```
description: |
  This is a multi-line string.
  It preserves new lines.
```

## Folded Block (`>`) – Joins into One Line

```
description: >
  This is a multi-line string.
  It will be converted into a single line.
```

## 7. Boolean, Null, and Other Data Types in YAML

```
is_active: true
is_admin: false
unknown_value: null
```

Equivalent JSON:

```
{
  "is_active": true,
  "is_admin": false,
  "unknown_value": null
}
```

## 8. YAML Best Practices

- **Use 2 spaces per indentation level** (avoid tabs).
- **Always maintain consistent indentation**.
- **Quote special characters (**`**:**` **or** `**@**`**) to avoid errors**:

```
email: "user@example.com"
```

- **Avoid using tabs** — YAML does not support them.
- **Use meaningful keys** — Avoid ambiguous naming.