# Ejercicios Clase

## 1. Function that checks if a given number is positive, negative, or zero.

**Reglas Resumidas:**

- `N > 0` → Positive
- `N = 0` → Zero
- `N < 0` → Negative

**Test Cases:**

| Caso | Input | Output   |
| :--- | :---- | :------- |
| 1    | 5     | Positive |
| 2    | 0     | Zero     |
| 3    | -5    | Negative |

---

## 2. Function that validates user passwords.

The password validation rules are as follows:
The password must be at least 8 characters long.
The password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (!, @, #, $, %, or &).

**Reglas Resumidas:**

- Longitud >= 8
- Contiene: [A-Z], [a-z], [0-9], [!@#$%&]

**Test Cases:**

| Caso | >= 8 char | Mayúscula | Minúscula | Dígito | Especial | Input      | Output    |
| :--- | :-------- | :-------- | :-------- | :----- | :------- | :--------- | :-------- |
| 1    | Sí        | Sí        | Sí        | Sí     | Sí       | `Hola123&` | Válido    |
| 2    | Sí        | Sí        | Sí        | Sí     | No       | `Hola1234` | No válido |
| 3    | Sí        | Sí        | Sí        | No     | No       | `Holaaaaa` | No válido |
| 4    | Sí        | Sí        | No        | No     | No       | `HOLAAAAA` | No válido |
| 5    | No        | No        | Sí        | No     | No       | `hola`     | No válido |

---

## 3. Function that calculates the discount for a customer's purchase based on the total amount.

The discount rules are as follows:
If the total amount is less than 100, no discount is applied.
If the total amount is between 100 and 500 (inclusive), a 10% discount is applied.
If the total amount is greater than 500, a 20% discount is applied.

**Reglas Resumidas:**

- `Total < 100` → 0%
- `100 <= Total <= 500` → 10%
- `Total > 500` → 20%

**Test Cases:**

| Caso | Input (Monto) | Output (% Descuento) |
| :--- | :------------ | :------------------- |
| 1    | 99.99         | 0                    |
| 2    | 100           | 10                   |
| 3    | 499.99        | 10                   |
| 4    | 500           | 10                   |
| 5    | 500.01        | 20                   |

---

## 4. Function that processes user orders in an e-commerce system.

The function calculates the total price of the items in the order, applying different discounts based on the quantity of each item. The discount rules are as follows:
If the quantity of a single item is between 1 and 5 (inclusive), no discount is applied.
If the quantity of a single item is between 6 and 10 (inclusive), a 5% discount is applied.
If the quantity of a single item is greater than 10, a 10% discount is applied.

**Reglas Resumidas:**

- `1-5` items → 0%
- `6-10` items → 5%
- `> 10` items → 10%

**Test Cases:**

| Caso | Input (Cantidad) | Output (% Descuento) |
| :--- | :--------------- | :------------------- |
| 1    | 1                | 0                    |
| 2    | 5                | 0                    |
| 3    | 6                | 5                    |
| 4    | 10               | 5                    |
| 5    | 11               | 10                   |

---

## 5. Function that calculates shipping costs.

The function calculates shipping costs based on the total weight of the items in the order and the shipping method chosen by the customer. The shipping cost rules are as follows:

**For standard shipping:**

- If the total weight is less than or equal to 5 kg, the cost is $10.
- If the total weight is between 5 and 10 kg (inclusive), the cost is $15.
- If the total weight is greater than 10 kg, the cost is $20.

**For express shipping:**

- If the total weight is less than or equal to 5 kg, the cost is $20.
- If the total weight is between 5 and 10 kg (inclusive), the cost is $30.
- If the total weight is greater than 10 kg, the cost is $40.

**Reglas Resumidas:**

| Peso (Kg) | Standard | Express |
| :-------- | :------- | :------ |
| `<= 5`    | $10      | $20     |
| `6 - 10`  | $15      | $30     |
| `> 10`    | $20      | $40     |

**Test Cases:**

| Caso | Peso (Input) | Método   | Costo (Output) |
| :--- | :----------- | :------- | :------------- |
| 1    | 4            | Standard | 10             |
| 2    | 5            | Standard | 10             |
| 3    | 8            | Standard | 15             |
| 4    | 11           | Standard | 20             |
| 5    | 5            | Express  | 20             |
| 6    | 10           | Express  | 30             |
| 7    | 15           | Express  | 40             |
