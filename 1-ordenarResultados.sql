
#------------------------------------Ordenación de los resultados
#------------------------------------Uso de la cláusula ORDER BY

SELECT<select_list>
FROM <table_source>
ORDER BY <order_by_list> [ASC|DESC];

#--------------------------------------Dirección de la ordenación

SELECT ProductCategoryID AS Category, ProductName
FROM Production.Product
ORDER BY Category ASC, Price DESC;

#------------------------------------Limitación de los resultados ordenados
--------------------------------------Usar la cláusula TOP

SELECT TOP (N) <column_list>
FROM <table_source>
WHERE <search_condition>
ORDER BY <order list> [ASC|DESC];

SELECT TOP 10 Name, ListPrice
FROM Production.Product
ORDER BY ListPrice DESC;

#--------------------------------------Uso de WITH TIES

SELECT TOP 10 WITH TIES Name, ListPrice
FROM Production.Product
ORDER BY ListPrice DESC;

#--------------------------------------Uso de PERCENT
SELECT TOP 10 PERCENT Name, ListPrice
FROM SalesLT.Product
ORDER BY ListPrice DESC;

#--------------------------------------Sintaxis de OFFSET-FETCH
OFFSET { integer_constant | offset_row_count_expression } { ROW | ROWS }
[FETCH { FIRST | NEXT } {integer_constant | fetch_row_count_expression } { ROW | ROWS } ONLY]

#--------------------------------------Uso de OFFSET-FETCH
SELECT ProductID, ProductName, ListPrice
FROM Production.Product
ORDER BY ListPrice DESC 
OFFSET 0 ROWS --Skip zero rows
FETCH NEXT 10 ROWS ONLY; --Get the next 10

#--------------------------------------Eliminación de duplicados
Example
SELECT City, CountryRegion
FROM Production.Supplier
ORDER BY CountryRegion, City;

SELECT DISTINCT City, CountryRegion
FROM Production.Supplier
ORDER BY CountryRegion, City;

#--------------------------------------Filtrado de los datos con predicados
--------------------------------------La estructura de la cláusula WHERE

SELECT ProductCategoryID AS Category, ProductName
FROM Production.Product
WHERE ProductCategoryID = 2;

SELECT ProductCategoryID AS Category, ProductName
FROM Production.Product
WHERE ListPrice < 10.00;

#--------------------------------------IS NULL/IS NOT NULL
SELECT ProductCategoryID AS Category, ProductName
FROM Production.Product
WHERE ProductName IS NOT NULL;

#--------------------------------------Varias condiciones

SELECT ProductCategoryID AS Category, ProductName
FROM Production.Product
WHERE ProductCategoryID = 2
    AND ListPrice < 10.00;

#--------------------------------------Operadores de comparación
#--------------------------------------IN

SELECT ProductCategoryID AS Category, ProductName
FROM Production.Product
WHERE ProductCategoryID = 2
    OR ProductCategoryID = 3
    OR ProductCategoryID = 4;

SELECT ProductCategoryID AS Category, ProductName
FROM Production.Product
WHERE ProductCategoryID IN (2, 3, 4);

#--------------------------------------BETWEEN

SELECT ProductCategoryID AS Category, ProductName
FROM Production.Product
WHERE ListPrice >= 1.00
    AND ListPrice <= 10.00;

SELECT ProductCategoryID AS Category, ProductName
FROM Production.Product
WHERE ListPrice BETWEEN 1.00 AND 10.00;

SELECT ProductName, ModifiedDate
FROM Production.Product
WHERE ModifiedDate BETWEEN '2012-01-01' AND '2012-12-31';

SELECT ProductName, ListPrice, ModifiedDate
FROM Production.Product
WHERE ModifiedDate BETWEEN '2012-01-01 00:00:00.000' AND '2012-12-31 23:59:59.999';

SELECT ProductName, ListPrice, ModifiedDate
FROM Production.Product
WHERE ModifiedDate >= '2012-01-01' 
    AND ModifiedDate < '2013-01-01';

#--------------------------------------LIKE

SELECT Name, ListPrice
FROM SalesLT.Product
WHERE Name LIKE '%mountain%';

SELECT ProductName, ListPrice
FROM SalesLT.Product
WHERE ProductName LIKE 'Mountain Bike Socks, _';

SELECT ProductName, ListPrice
FROM SalesLT.Product
WHERE ProductName LIKE 'Mountain-[0-9][0-9][0-9] %, [0-9][0-9]';