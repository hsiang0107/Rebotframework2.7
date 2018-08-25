USE AdventureWorks
DECLARE @PrdName varchar(30) = 'test7'
DECLARE @guid uniqueidentifier = '2BE3BE36-D9A2-4EEE-B593-CD895D975689'
Insert into Production.ProductCategory
(Name, rowguid)
values
(@PrdName, @guid)
GO