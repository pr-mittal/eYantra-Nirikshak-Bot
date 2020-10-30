--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code SCOR_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			SCOR_LUA.lua
*  Created:				07/10/2020
*  Last Modified:		07/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
]]--

-- getTheTopper function finds the student name who scored max, i.e. Topper's name from the scorelist created by readScoreList function
function getTheTopper(score_list)
	-- find the max score
    --score_list={{"sam",1},{"pam",2},{"dom",10},{"dsm",10},{"aum",10}}
    max=score_list[1][2]
    maxList={}
    -- print(#score_list)
    j=1
    for i=1,#score_list,1
    do
          if(max<score_list[i][2])
            then
            max=score_list[i][2]
            maxList={}
            j=1
          end
        --   print(max==score_list[i][2])
          if(max==score_list[i][2])
          then
            maxList[j]=score_list[i][1]
            j=j+1
            -- for key,str in pairs(maxList)
            -- do 
            --     print(str)
            -- end
          end
    end
    -- for key,str in pairs(maxList)
    -- do 
    --     print(str)
    -- end
    table.sort(maxList,function(a, b) return a:lower() < b:lower()end)
    for key,value in pairs(maxList)
    do
        print(value)    
    end
end

-- readScoreList function creates the scorelist table from input
function readScoreList(N)
    local scorelist={}
    
    for i=1,N,1
    do
      str=io.read()
      scorelist[i]={}
      for key, value in string.gmatch(str, "(%w+)%s+(%w+)") 
      do
        -- print(key)
        scorelist[i]={key,tonumber(value)}
      --> key: foo, value: bar
      --> key: bar, value: foo
      end
    end
    --for key, value in pairs(scorelist) 
      --do
        --print(key,value)
      --end
      -- print(scorelist[i][2])
      return scorelist
    end

-- for each case, call the readScoreList and getTheTopper functions to get the scores of students and then find the student name who scored max, i.e. Topper's name
tc = tonumber(io.read())
for i=1,tc
do
	local N=tonumber(io.read())
  -- print(N)
	score_list=readScoreList(N);
	-- print(score_list)
  getTheTopper(score_list)
  -- print(getTheTopper({{"Sam",1},{"Sam1",4},{"Sam2",10},{"Sam3",2}}))
end

