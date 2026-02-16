# Black-box tests

**Alan Varela**
15 feb 2026

## Equivalence Partitioning

1. Function that validates credit card numbers.
   - Valid card numbers: Length between 13 and 16 digits, containing only numeric digits.

| Test Case                          | Input Data          | Expected Result |
| :--------------------------------- | :------------------ | :-------------- |
| **Min valid length (13 digits)**   | `1234567890123`     | **Valid**       |
| **Max valid length (16 digits)**   | `1234567890123456`  | **Valid**       |
| **Below min length (12 digits)**   | `123456789012`      | **Invalid**     |
| **Above max length (17 digits)**   | `12345678901234567` | **Invalid**     |
| **Contains letter (Char)**         | `1234567890abc`     | **Invalid**     |


2. Function that validates dates.
   - Valid years: Between 1900 and 2100.
   - Valid months: Between 1 and 12.
   - Valid days: Between 1 and 31.

| Test Case                 | Input Data   | Expected Result |
| :------------------------ | :----------- | :-------------- |
| **Min valid year (1900)** | `1900-01-01` | **Valid**       |
| **Max valid year (2100)** | `2100-12-31` | **Valid**       |
| **Below min year (1899)** | `1899-12-31` | **Invalid**     |
| **Above max year (2101)** | `2101-01-01` | **Invalid**     |
| **Invalid Month (13)**    | `2023-13-01` | **Invalid**     |
| **Invalid Day (32)**      | `2023-01-32` | **Invalid**     |

3. Function that checks the eligibility of a passenger to book a flight.
   - Eligible ages: Between 18 and 65.
   - Frequent flyers: True or False.

| Test Case                         | Input Data             | Expected Result  |
| :-------------------------------- | :--------------------- | :--------------- |
| **Min valid age (18)**            | Age: `18`, FF: `False` | **Eligible**     |
| **Max valid age (65)**            | Age: `65`, FF: `False` | **Eligible**     |
| **Below min age (17)**            | Age: `17`, FF: `True`  | **Not Eligible** |
| **Above max age (66)**            | Age: `66`, FF: `True`  | **Not Eligible** |
| **Frequent Flyer Status (True)**  | Age: `30`, FF: `True`  | **Eligible**     |
| **Frequent Flyer Status (False)** | Age: `30`, FF: `False` | **Eligible**     |

4. Function that validates URLs.
   - Valid URLs: Length less than or equal to 255, starting with "http://" or "https://".

| Test Case                        | Input Data               | Expected Result |
| :------------------------------- | :----------------------- | :-------------- |
| **Valid prefix (http)**          | `http://iteso.com`       | **Valid**       |
| **Valid prefix (https)**         | `https://iteso.com`      | **Valid**       |
| **Invalid prefix (ftp)**         | `ftp://iteso.com`        | **Invalid**     |
| **Invalid prefix (text)**        | `www.iteso.com`          | **Invalid**     |
| **Max valid length (255 chars)** | `https://` + [247 chars] | **Valid**       |
| **Above max length (256 chars)** | `https://` + [248 chars] | **Invalid**     |

## Boundary Value Analysis

1. Function that calculates the eligibility of a person for a loan based on their income and credit score.
   The eligibility rules are as follows:
   - If the income is less than $30,000, the person is not eligible for a loan.
   - If the income is between $30,000 and $60,000 (inclusive) and the credit score is above 700, the person is eligible for a standard loan.
   - If the income is between $30,000 and $60,000 (inclusive) and the credit score is below or equal to 700, the person is eligible for a secured loan.
   - If the income is greater than $60,000 and the credit score is above 750, the person is eligible for a premium loan.
   - If the income is greater than $60,000 and the credit score is between 700 and 750 (inclusive), the person is eligible for a standard loan.

| Test Case                              | Input Data                     | Expected Result   |
| :------------------------------------- | :----------------------------- | :---------------- |
| **Income below min boundary (29,999)** | Income: `29,999`               | **Not Eligible**  |
| **Income min boundary (30,000)**       | Income: `30,000`, Score: `600` | **Secured Loan**  |
| **Score boundary low (700)**           | Income: `45,000`, Score: `700` | **Secured Loan**  |
| **Score boundary mid (701)**           | Income: `45,000`, Score: `701` | **Standard Loan** |
| **Income max boundary (60,000)**       | Income: `60,000`, Score: `720` | **Standard Loan** |
| **Income above max (60,001)**          | Income: `60,001`, Score: `720` | **Standard Loan** |
| **Score boundary high (750)**          | Income: `70,000`, Score: `750` | **Standard Loan** |
| **Score above high (751)**             | Income: `70,000`, Score: `751` | **Premium Loan**  |

2. Function that determines the category of a product in an e-commerce system based on its price.
   The product categories and pricing rules are as follows:
   - Category A: Products priced between $10 and $50 (inclusive).
   - Category B: Products priced between $51 and $100 (inclusive).
   - Category C: Products priced between $101 and $200 (inclusive).
   - Category D: Products priced above $200.

| Test Case           | Input Data   | Expected Result |
| :------------------ | :----------- | :-------------- |
| **Below range (9)** | Price: `9`   | **Invalid**     |
| **Min Cat A (10)**  | Price: `10`  | **Category A**  |
| **Max Cat A (50)**  | Price: `50`  | **Category A**  |
| **Min Cat B (51)**  | Price: `51`  | **Category B**  |
| **Max Cat B (100)** | Price: `100` | **Category B**  |
| **Min Cat C (101)** | Price: `101` | **Category C**  |
| **Max Cat C (200)** | Price: `200` | **Category C**  |
| **Min Cat D (201)** | Price: `201` | **Category D**  |

3. Function that calculates the cost of shipping for packages based on their weight and dimensions.
   The shipping cost rules are as follows:
   - If the weight of the package is less than or equal to 1 kg and the dimensions (length, width, and height) are each less than or equal to 10 cm, the cost is $5.
   - If the weight is between 1 and 5 kg (inclusive) and the dimensions are each between 11 and 30 cm (inclusive), the cost is $10.
   - If the weight is greater than 5 kg or any of the dimensions is greater than 30 cm, the cost is $20.

| Test Case                     | Input Data            | Expected Result |
| :---------------------------- | :-------------------- | :-------------- |
| **Max Tier 1 Weight (1kg)**   | W: `1kg`, D: `10cm`   | **$5**          |
| **Max Tier 1 Dim (10cm)**     | W: `1kg`, D: `10cm`   | **$5**          |
| **Min Tier 2 Weight (1.1kg)** | W: `1.1kg`, D: `10cm` | **$10**         |
| **Min Tier 2 Dim (11cm)**     | W: `1kg`, D: `11cm`   | **$10**         |
| **Max Tier 2 Weight (5kg)**   | W: `5kg`, D: `30cm`   | **$10**         |
| **Max Tier 2 Dim (30cm)**     | W: `5kg`, D: `30cm`   | **$10**         |
| **Min Tier 3 Weight (5.1kg)** | W: `5.1kg`, D: `15cm` | **$20**         |
| **Min Tier 3 Dim (31cm)**     | W: `3kg`, D: `31cm`   | **$20**         |

## Decision Table

1. Create the decision table for a system that provides weather advisories based on temperature and humidity.
   The rules are:
   - Weather recommendation "High temperature and humidity. Stay hydrated." for temperature > 30 and humidity > 70.
   - Weather recommendation "Low temperature. Don't forget your jacket!" for temperature < 0 and any humidity.
   - No weather recommendation for any other temperature and humidity combination.

| Test Case                           | Input Data       | Expected Result             |
| :---------------------------------- | :--------------- | :-------------------------- |
| **High Temp & High Hum (>30, >70)** | T: `31`, H: `71` | **"High temp/humidity..."** |
| **High Temp & Low Hum (>30, <=70)** | T: `31`, H: `70` | **No recommendation**       |
| **Low Temp (<0)**                   | T: `-1`, H: `50` | **"Low temperature"**       |
| **Normal conditions (20, 50)**      | T: `20`, H: `50` | **No recommendation**       |

2. Create the decision table for a system that authenticates users based on their username and password.
   The rules are:
   - Returns "Admin" for username "admin" and password "admin123".
   - Returns "User" for any other username with at least 5 characters and password with at least 8 characters.
   - Returns "Invalid" if the username or password lenghts are not met.

**Rules:** Admin/admin123, User (len>=5, pass>=8), Invalid.

| Test Case                    | Input Data                  | Expected Result |
| :--------------------------- | :-------------------------- | :-------------- |
| **Exact Admin Creds**        | U: `admin`, P: `admin123`   | **"Admin"**     |
| **Valid User (Standard)**    | U: `usuario`, P: `password` | **"User"**      |
| **Invalid User (Too short)** | U: `user`, P: `password`    | **"Invalid"**   |
| **Invalid Pass (Too short)** | U: `usuario`, P: `pass`     | **"Invalid"**   |
| **Admin User / Wrong Pass**  | U: `admin`, P: `wrong`      | **"User"**      |
