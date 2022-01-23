IF EXISTS (SELECT * FROM Products WHERE id = ?)
BEGIN
--do what you need if exists
END
ELSE
BEGIN
--do what needs to be done if not
END