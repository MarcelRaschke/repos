CREATE TABLE [dbo].[__MigrationLog]
(
	[SqlHash] BINARY(64) NULL, 
    [StartTime] DATETIME2 NULL, 
    [EndTime] DATETIME2 NULL, 
    [SqlText] NVARCHAR(MAX) NULL,
    [WasSuccessful] BIT NULL DEFAULT 0, 
    [Error] NVARCHAR(MAX) NULL,
    [Author] NVARCHAR(250) NULL, 
    [Build] NVARCHAR(50) NULL,
	CONSTRAINT [PK_MigrationLog] PRIMARY KEY CLUSTERED ([SqlHash] ASC),
)
