-- WORK 1
Create Table Stationary(S_ID char(4), SNAME varchar(8), Company varchar(8), Price int);
Insert into Stationary values('DP01', 'Dot Pen', 'Cello',10);
Insert into Stationary values('PL02', 'Pencil', 'DOMS',5);
Insert into Stationary values('ER05', 'Erasor', 'DOMS',5);
Insert into Stationary values('PL01', 'Pencil', 'Natraj',4);
Insert into Stationary values('GP01', 'Gel Pen', 'Rotomac',8);

Create Table distributor(D_ID int, Distributor varchar(20), City varchar(8), S_ID char(4));
Insert into distributor values(1, 'Excellent Stationary', 'Surat' ,'PL01');
Insert into distributor values(2, 'Vidhya Stationary', 'Baroda' ,'GP02');
Insert into distributor values(3, 'Student Book Shop', 'Surat' ,'DP01');
Insert into distributor values(4, 'Pupils Corner', 'Surat' ,'PL02');
Insert into distributor values(5, 'Abhyass Stationary', 'Baroda' ,'DP01');

Select distinct City from distributor;
Select max(Price), min(Price), Company from Stationary Group by Company;
Select S.SNAME, S.Company, D.Distributor, D.City from Stationary as S, distributor as D Where S.S_ID=D.S_ID;
Select * from Stationary, distributor Where(Stationary.S_ID=distributor.S_ID and distributor.Distributor like '%stationary%');


-- WORK 2
Create Table Customer(CustomerID char(4), CustomerName varchar(8), City varchar(10), MobileNo char(10));
Insert into Customer values('C111', 'Abhishek', 'Ahmedabad','9999999999');
Insert into Customer values('C132', 'Bhavik', 'Anand','7799779977');
Insert into Customer values('C135', 'Chandani', 'Baroda','8856895485');
Insert into Customer values('C145', 'Dhara', 'Ahmedabad','7456879652');
Insert into Customer values('C121', 'Divya', 'Anand','9015123569');

Create Table Orders(OrderID char(4), OrderDate date, OrderAmt int, CustomerID char(4));
Insert into Orders values('O111', '2022-04-15', 1500,'C111');
Insert into Orders values('O112', '2022-05-20', 1800,'C121');
Insert into Orders values('O113', '2022-05-31', 1000,'C199');
Insert into Orders values('O131', '2022-06-12', 1400,'C135');

Select C.CustomerID, C.CustomerName, O.OrderAmt from Customer as C, Orders as O Where(C.City='Ahmedabad' and C.CustomerID = O.CustomerID);
Select * from Orders Order By OrderAmt Desc;
Select O.OrderID, O.OrderDate, C.CustomerName, C.MobileNo from Customer as C, Orders as O Where(C.CustomerName like '%k' and C.CustomerName like '%h%' and C.CustomerID = O.CustomerID);
Select sum(O.OrderAmt), C.City from Customer as C, Orders as O Where C.CustomerID=O.CustomerID Group By C.City;