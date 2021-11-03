-- INSERT INTO <sampleTable>  
SELECT TOP 10 
	ID as Dynacard_ID
	, API14
	, SurfaceUnitAnalysis
	, SUA.Optimal_Counterbalance 
	, SUA.GearBoxRating 
FROM dbo.RodPump_DynaCardsJson as A

CROSS APPLY OPENJSON (A.SurfaceUnitAnalysis)
	WITH (
		Optimal_Counterbalance	NUMERIC(6, 2) N'$."Optimal Counterbalance (in-lb x 1000)"'
		, GearBoxRating			NUMERIC(6, 2) N'$.GearBoxRating'
		)
 as SUA

WHERE ID > 7588639

-- format of SurfaceUnitAnalysis JSON is:
-- {"Optimal Counterbalance (in-lb x 1000)": 971.5, "Actual Counterbalance (in-lb x 1000)": 0.0, "GearBoxRating": 640.0}
