CREATE PROC [dev].[MyStoredProc]
@param1 int,
@param2 int
AS
BEGIN
SELECT @param1, @param2
END