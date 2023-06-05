= Pick(Match('$(vSelectError)','1_APE','AE')
	, IF(Aggr(AVG({<[INDEX_$(vColumnY)]=P([INDEX_$(vColumnY)]), [구분_Y]={"$(vSelectError)"}, [지표OLD_Y]={"$(vColumnY)"}>} [VALUE_Y]),[INDEX_$(vColumnY)])
    	=MIN(Aggr(AVG({<[INDEX_$(vColumnY)]=P([INDEX_$(vColumnY)]), [구분_Y]={"$(vSelectError)"}, [지표OLD_Y]={"$(vColumnY)"}>} [VALUE_Y]),[INDEX_$(vColumnY)]))
    	, 'RED'
		, If(Aggr(AVG({<[INDEX_$(vColumnY)]=P([INDEX_$(vColumnY)]), [구분_Y]={"$(vSelectError)"}, [지표OLD_Y]={"$(vColumnY)"}>} [VALUE_Y]),[INDEX_$(vColumnY)])
    		> Alt(vLclError, AVG(Total {<[INDEX_$(vColumnY)]=P([INDEX_$(vColumnY)]), [구분_Y]={"$(vSelectError)"}, [지표OLD_Y]={"$(vColumnY)"}>} [VALUE_Y])
						- 3 * Stdev(Total {<[INDEX_$(vColumnY)]=P([INDEX_$(vColumnY)]), [구분_Y]={"$(vSelectError)"}, [지표OLD_Y]={"$(vColumnY)"}>} [VALUE_Y]))
            , '#545352'
            , '#FF5722')
        )
    , IF(Aggr(AVG({<[INDEX_$(vColumnY)]=P([INDEX_$(vColumnY)]), [구분_Y]={"$(vSelectError)"}, [지표OLD_Y]={"$(vColumnY)"}>} [VALUE_Y]),[INDEX_$(vColumnY)])
    	=MAX(Aggr(AVG({<[INDEX_$(vColumnY)]=P([INDEX_$(vColumnY)]), [구분_Y]={"$(vSelectError)"}, [지표OLD_Y]={"$(vColumnY)"}>} [VALUE_Y]),[INDEX_$(vColumnY)]))
    	, 'RED'
        , If(Aggr(AVG({<[INDEX_$(vColumnY)]=P([INDEX_$(vColumnY)]), [구분_Y]={"$(vSelectError)"}, [지표OLD_Y]={"$(vColumnY)"}>} [VALUE_Y]),[INDEX_$(vColumnY)])
	    		< Alt(vUclError, AVG(Total {<[INDEX_$(vColumnY)]=P([INDEX_$(vColumnY)]), [구분_Y]={"$(vSelectError)"}, [지표OLD_Y]={"$(vColumnY)"}>} [VALUE_Y])
						+ 3 * Stdev(Total {<[INDEX_$(vColumnY)]=P([INDEX_$(vColumnY)]), [구분_Y]={"$(vSelectError)"}, [지표OLD_Y]={"$(vColumnY)"}>} [VALUE_Y]))
            , '#545352'
            , '#FF5722')
        )
    )
    
	test111111