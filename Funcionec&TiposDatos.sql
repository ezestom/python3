#Examen de la instrucción SELECT

#mySQL
SELECT OrderDate, COUNT(OrderID) AS Orders
FROM Sales.SalesOrder
WHERE Status = 'Shipped'
GROUP BY OrderDate
HAVING COUNT(OrderID) > 1
ORDER BY OrderDate DESC;

#ServerSQL
FROM Sales.SalesOrder
WHERE Status = 'Shipped'
GROUP BY OrderDate 
HAVING COUNT(OrderID) > 1
SELECT OrderDate, COUNT(OrderID) AS Orders
ORDER BY OrderDate DESC;

#Selección de todas las columnas
SELECT * FROM Production.Product;

#Selección de columnas específicas
SELECT ProductID, Name, ListPrice, StandardCost
FROM Production.Product;

#Selección de expresiones
SELECT ProductID,
      Name + '(' + ProductNumber + ')',
  ListPrice - StandardCost
FROM Production.Product;

#Especificación de alias de columna
SELECT ProductID AS ID,
      Name + '(' + ProductNumber + ')' AS ProductName,
  ListPrice - StandardCost AS Markup
FROM Production.Product;

#? Trabajo con tipos de datos

Valor numérico
Exacto
bigint
numeric
bit
smallint
decimal
smallmoney
int
tinyint
money
Numéricos aproximados
float
real
Fecha y Hora
date
datetimeoffset
datetime2
smalldatetime
datetime
time
Cadenas de caracteres
char
varchar
text
Cadenas de caracteres Unicode
nchar
nvarchar
ntext
Cadenas binarias
binary
varbinary
image
Otros tipos de datos
cursor
rowversion
hierarchyid
uniqueidentifier
sql_variant
xml
Tipos de geometría espacial
Tipos de geografía espacial
table

#!CAST y TRY_CAST
SELECT CAST(ProductID AS varchar(4)) + ': ' + Name AS ProductName
FROM Production.Product;

SELECT CAST(Size AS integer) As NumericSize
FROM Production.Product;  # --> Error: Error de conversión al convertir el valor nvarchar "M" al tipo de datos int.

SELECT TRY_CAST(Size AS integer) As NumericSize
FROM Production.Product;

#!CONVERT y TRY_CONVERT
SELECT CONVERT(varchar(4), ProductID) + ': ' + Name AS ProductName
FROM Production.Product;

SELECT SellStartDate,
       CONVERT(varchar(20), SellStartDate) AS StartDate,
       CONVERT(varchar(10), SellStartDate, 101) AS FormattedStartDate 
FROM SalesLT.Product;


#!PARSE y TRY_PARSE
SELECT PARSE('01/01/2021' AS date) AS DateValue,
   PARSE('$199.99' AS money) AS MoneyValue;

#!STR
SELECT ProductID,  '$' + STR(ListPrice) AS Price
FROM Production.Product;

#!Controlar valores NULL
ISNULL
SELECT FirstName,
      ISNULL(MiddleName, 'None') AS MiddleIfAny,
      LastName
FROM Sales.Customer;

!#COALESCE
SELECT COALESCE ( expression1, expression2, [ ,...n ] )

SELECT EmployeeID,
      COALESCE(HourlyRate * 40,
                WeeklySalary,
                Commission * SalesQty) AS WeeklyEarnings
FROM HR.Wages;

#NULLIF
SELECT SalesOrderID,
      ProductID,
      UnitPrice,
      NULLIF(UnitPriceDiscount, 0) AS Discount
FROM Sales.SalesOrderDetail;