#Sort and Filter Query Results

SELECT Name, ListPrice
FROM SalesLT.Product;

SELECT Name, ListPrice
FROM SalesLT.Product
ORDER BY Name;

SELECT Name, ListPrice
FROM SalesLT.Product
ORDER BY ListPrice;

SELECT Name, ListPrice
FROM SalesLT.Product
ORDER BY ListPrice DESC;

SELECT Name, ListPrice
FROM SalesLT.Product
ORDER BY ListPrice DESC, Name ASC;

#Restrict results using TOP

SELECT TOP (20) Name, ListPrice
FROM SalesLT.Product
ORDER BY ListPrice DESC;

SELECT TOP (20) WITH TIES Name, ListPrice
FROM SalesLT.Product
ORDER BY ListPrice DESC;

SELECT TOP (20) PERCENT WITH TIES Name, ListPrice
FROM SalesLT.Product
ORDER BY ListPrice DESC;

#Retrieve pages of results with OFFSET and FETCH

SELECT Name, ListPrice
FROM SalesLT.Product
ORDER BY Name OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY;

SELECT Name, ListPrice
FROM SalesLT.Product
ORDER BY Name OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;

#Use the ALL and DISTINCT options

SELECT Color
FROM SalesLT.Product;

SELECT ALL Color
FROM SalesLT.Product;

SELECT DISTINCT Color
FROM SalesLT.Product;

SELECT DISTINCT Color, Size
FROM SalesLT.Product;

#Filter results with the WHERE clause

SELECT Name, Color, Size
FROM SalesLT.Product
WHERE ProductModelID = 6
ORDER BY Name;

SELECT Name, Color, Size
FROM SalesLT.Product
WHERE ProductModelID <> 6
ORDER BY Name;

SELECT Name, ListPrice
FROM SalesLT.Product
WHERE ListPrice > 1000.00
ORDER BY ListPrice;

SELECT Name, ListPrice
FROM SalesLT.Product
WHERE Name LIKE 'HL Road Frame %';

SELECT Name, ListPrice
FROM SalesLT.Product
WHERE ProductNumber LIKE 'FR-_[0-9][0-9]_-[0-9][0-9]';

SELECT Name, ListPrice
FROM SalesLT.Product
WHERE SellEndDate IS NOT NULL;

SELECT Name
FROM SalesLT.Product
WHERE SellEndDate BETWEEN '2006/1/1' AND '2006/12/31';

SELECT ProductCategoryID, Name, ListPrice
FROM SalesLT.Product
WHERE ProductCategoryID IN (5,6,7);

SELECT ProductCategoryID, Name, ListPrice, SellEndDate
FROM SalesLT.Product
WHERE ProductCategoryID IN (5,6,7) AND SellEndDate IS NULL;

SELECT Name, ProductCategoryID, ProductNumber
FROM SalesLT.Product
WHERE ProductNumber LIKE 'FR%' OR ProductCategoryID IN (5,6,7);

#Challenge
SELECT DISTINCT City, StateProvince
FROM SalesLT.Address
ORDER BY City

SELECT TOP (10) PERCENT WITH TIES Name
FROM SalesLT.Product
ORDER BY We

SELECT Name, Color, Size
FROM SalesLT.Product
WHERE ProductModelID = 1;

SELECT ProductNumber, Name
FROM SalesLT.Product
WHERE Color IN ('Black','Red','White') AND Size IN ('S','M');

SELECT ProductNumber, Name, ListPrice
FROM SalesLT.Product
WHERE ProductNumber LIKE 'BK-%';

SELECT ProductNumber, Name, ListPrice
FROM SalesLT.Product
WHERE ProductNumber LIKE 'BK-[^R]%-[0-9][0-9]';