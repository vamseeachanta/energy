-- INSERT INTO <sampleTable>  
SELECT TOP 10 
	ID as Dynacard_ID
	, API14
	, SurfaceUnitAnalysis
	, SUA.Optimal_Counterbalance 
	, SUA.GearBoxRating 
	, SUA.CrankAngle 
	, SUA.CrankAngle_element 
	, SUA.BalancedTorqueStatistics_max 
	, SUA.BalancedTorqueStatistics_min 
	, SUA.BalancedTorqueStatistics_abs_max 
FROM dbo.RodPump_DynaCardsJson as A

CROSS APPLY OPENJSON (A.SurfaceUnitAnalysis)
	WITH (
		Optimal_Counterbalance	            NUMERIC(6, 2)       N'$."Optimal Counterbalance (in-lb x 1000)"'
		, GearBoxRating			            NUMERIC(6, 2)       N'$.GearBoxRating'
        -- AS JSON Only works with NVARCHAR (MAX) as of MS SQL Version 15.0
        , CrankAngle						NVARCHAR (MAX)      N'$.CrankAngle' as JSON
        , CrankAngle_element                NVARCHAR (2000)     N'$.CrankAngle[1]'
        , BalancedTorqueStatistics_max      NUMERIC(6, 2)       N'$.BalancedTorqueStatistics.max'
        , BalancedTorqueStatistics_min      NUMERIC(6, 2)       N'$.BalancedTorqueStatistics.min'
        , BalancedTorqueStatistics_abs_max  NUMERIC(6, 2)       N'$.BalancedTorqueStatistics.abs_max'
		)
 as SUA

WHERE ID > 7588639

-- format of SurfaceUnitAnalysis JSON is:
-- {"Optimal Counterbalance (in-lb x 1000)": 971.5, "Actual Counterbalance (in-lb x 1000)": 0.0, "GearBoxRating": 640.0, "CrankAngle": [-2.23, -1.16, 0.42, 1.62], "BalancedTorqueStatistics": {"max": 197.6, "min": -127.9, "abs_max": 197.6}}
