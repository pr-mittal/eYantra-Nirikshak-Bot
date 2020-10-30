--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code STAR_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			STAR_LUA.lua
*  Created:				07/10/2020
*  Last Modified:		07/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
]]--

-- generatePattern function to print the pattern of start(*) and hash(#)
function generatePattern()
	n = tonumber(io.read())
  local str5="****#"
  for i=math.floor(n/5),0,-1
  do 
    local x=(n-i*5)%5
      for j=x,0,-1
      do
        io.write(string.rep(str5,i))
        print(string.rep("*",j))
        n=n-1
      end
    
  end

end

-- read the test cases input
tc = tonumber(io.read())

-- for each case, call the generatePattern function to print the pattern
for i=1,tc
do
	generatePattern()
end
